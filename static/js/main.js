// Main JavaScript for Smart Image Updater

// Global variables
let selectedImageUrl = null;
let isProcessing = false;

// Utility functions
function showLoading(message = 'Processing...') {
    const overlay = document.createElement('div');
    overlay.className = 'loading-overlay';
    overlay.innerHTML = `
        <div class="text-center text-white">
            <div class="loading-spinner mb-3"></div>
            <p>${message}</p>
        </div>
    `;
    document.body.appendChild(overlay);
}

function hideLoading() {
    const overlay = document.querySelector('.loading-overlay');
    if (overlay) {
        overlay.remove();
    }
}

function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insert at the top of the main content
    const main = document.querySelector('main .container');
    if (main) {
        main.insertBefore(alertDiv, main.firstChild);
    }
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Image selection functionality
function selectImage(imageUrl, element) {
    // Remove previous selections
    document.querySelectorAll('.image-option').forEach(option => {
        option.classList.remove('selected');
    });
    
    // Select current image
    element.classList.add('selected');
    selectedImageUrl = imageUrl;
    
    // Enable update button
    const updateBtn = document.getElementById('updateImageBtn');
    if (updateBtn) {
        updateBtn.disabled = false;
    }
}

// Update product image
async function updateProductImage(productId) {
    if (!selectedImageUrl) {
        showAlert('Please select an image first.', 'warning');
        return;
    }
    
    if (isProcessing) {
        return;
    }
    
    isProcessing = true;
    showLoading('Updating product image...');
    
    try {
        const response = await fetch(`/products/${productId}/update-image`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                image_url: selectedImageUrl
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showAlert('Image updated successfully!', 'success');
            
            // Reload page after a short delay
            setTimeout(() => {
                window.location.reload();
            }, 1500);
        } else {
            showAlert(`Error: ${data.error}`, 'danger');
        }
    } catch (error) {
        showAlert('An error occurred while updating the image.', 'danger');
        console.error('Error:', error);
    } finally {
        isProcessing = false;
        hideLoading();
    }
}

// Search images functionality
async function searchImages(productId, searchTerm) {
    if (!searchTerm.trim()) {
        showAlert('Please enter a search term.', 'warning');
        return;
    }
    
    showLoading('Searching for images...');
    
    try {
        const form = document.getElementById('searchForm');
        const formData = new FormData(form);
        
        const response = await fetch(`/products/${productId}/search`, {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            const html = await response.text();
            
            // Replace the search form with results
            const searchContainer = document.getElementById('searchContainer');
            if (searchContainer) {
                searchContainer.innerHTML = html;
            }
        } else {
            showAlert('Error searching for images.', 'danger');
        }
    } catch (error) {
        showAlert('An error occurred while searching.', 'danger');
        console.error('Error:', error);
    } finally {
        hideLoading();
    }
}

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

// Auto-save form data
function autoSaveForm(formId, key) {
    const form = document.getElementById(formId);
    if (!form) return;
    
    // Load saved data
    const savedData = localStorage.getItem(key);
    if (savedData) {
        const data = JSON.parse(savedData);
        Object.keys(data).forEach(name => {
            const input = form.querySelector(`[name="${name}"]`);
            if (input) {
                input.value = data[name];
            }
        });
    }
    
    // Save data on input change
    form.addEventListener('input', (e) => {
        const formData = new FormData(form);
        const data = {};
        for (let [name, value] of formData.entries()) {
            data[name] = value;
        }
        localStorage.setItem(key, JSON.stringify(data));
    });
}

// Image preview functionality
function previewImage(imageUrl, title = '') {
    const modal = new bootstrap.Modal(document.getElementById('imagePreviewModal'));
    const modalImage = document.getElementById('modalImage');
    const modalTitle = document.getElementById('modalTitle');
    
    modalImage.src = imageUrl;
    modalTitle.textContent = title || 'Image Preview';
    modal.show();
}

// Copy to clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('Copied to clipboard!', 'success');
    }).catch(() => {
        showAlert('Failed to copy to clipboard.', 'danger');
    });
}

// Initialize tooltips
function initTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Initialize popovers
function initPopovers() {
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
}

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Search suggestions
function setupSearchSuggestions(inputId, suggestionsId) {
    const input = document.getElementById(inputId);
    const suggestions = document.getElementById(suggestionsId);
    
    if (!input || !suggestions) return;
    
    const debouncedSearch = debounce(async (searchTerm) => {
        if (searchTerm.length < 2) {
            suggestions.style.display = 'none';
            return;
        }
        
        try {
            const response = await fetch(`/api/search-suggestions?q=${encodeURIComponent(searchTerm)}`);
            const data = await response.json();
            
            if (data.suggestions && data.suggestions.length > 0) {
                suggestions.innerHTML = data.suggestions.map(suggestion => 
                    `<div class="suggestion-item" onclick="selectSuggestion('${suggestion}')">${suggestion}</div>`
                ).join('');
                suggestions.style.display = 'block';
            } else {
                suggestions.style.display = 'none';
            }
        } catch (error) {
            console.error('Error fetching suggestions:', error);
        }
    }, 300);
    
    input.addEventListener('input', (e) => {
        debouncedSearch(e.target.value);
    });
    
    // Hide suggestions when clicking outside
    document.addEventListener('click', (e) => {
        if (!input.contains(e.target) && !suggestions.contains(e.target)) {
            suggestions.style.display = 'none';
        }
    });
}

function selectSuggestion(suggestion) {
    const input = document.querySelector('#searchTerm');
    if (input) {
        input.value = suggestion;
    }
    document.getElementById('searchSuggestions').style.display = 'none';
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap components
    initTooltips();
    initPopovers();
    
    // Setup form auto-save
    autoSaveForm('productForm', 'productFormData');
    autoSaveForm('searchForm', 'searchFormData');
    
    // Setup search suggestions
    setupSearchSuggestions('searchTerm', 'searchSuggestions');
    
    // Handle form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(form.id)) {
                e.preventDefault();
                showAlert('Please fill in all required fields.', 'warning');
            }
        });
    });
    
    // Handle image clicks for preview
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('image-preview')) {
            const imageUrl = e.target.src;
            const title = e.target.alt || 'Image Preview';
            previewImage(imageUrl, title);
        }
    });
    
    // Handle keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + Enter to submit forms
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            const activeForm = document.querySelector('form:focus-within');
            if (activeForm) {
                activeForm.requestSubmit();
            }
        }
        
        // Escape to close modals
        if (e.key === 'Escape') {
            const openModal = document.querySelector('.modal.show');
            if (openModal) {
                const modal = bootstrap.Modal.getInstance(openModal);
                if (modal) {
                    modal.hide();
                }
            }
        }
    });
});

// Export functions for global use
window.selectImage = selectImage;
window.updateProductImage = updateProductImage;
window.searchImages = searchImages;
window.previewImage = previewImage;
window.copyToClipboard = copyToClipboard;
window.selectSuggestion = selectSuggestion; 