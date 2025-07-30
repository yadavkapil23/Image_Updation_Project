import os
import re
from typing import List, Dict, Any
from urllib.parse import urlparse

def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe file system usage"""
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')
    # Limit length
    if len(filename) > 255:
        filename = filename[:255]
    return filename

def get_file_extension(url: str) -> str:
    """Extract file extension from URL"""
    parsed = urlparse(url)
    path = parsed.path.lower()
    
    # Common image extensions
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff']
    
    for ext in extensions:
        if path.endswith(ext):
            return ext
    
    return '.jpg'  # Default extension

def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f}{size_names[i]}"

def validate_url(url: str) -> bool:
    """Validate if URL is properly formatted"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def create_directory_if_not_exists(directory_path: str) -> bool:
    """Create directory if it doesn't exist"""
    try:
        os.makedirs(directory_path, exist_ok=True)
        return True
    except Exception:
        return False

def get_image_dimensions(image_path: str) -> tuple:
    """Get image dimensions without loading the entire image"""
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            return img.size
    except Exception:
        return (0, 0)

def is_valid_image_file(file_path: str) -> bool:
    """Check if file is a valid image"""
    try:
        from PIL import Image
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception:
        return False

def generate_search_suggestions(product_name: str) -> List[str]:
    """Generate search suggestions for product name"""
    suggestions = []
    
    # Add original name
    suggestions.append(product_name)
    
    # Add variations
    words = product_name.split()
    if len(words) > 1:
        # Add without last word
        suggestions.append(' '.join(words[:-1]))
        # Add without first word
        suggestions.append(' '.join(words[1:]))
        # Add first two words
        if len(words) >= 2:
            suggestions.append(' '.join(words[:2]))
    
    # Add common product terms
    common_terms = ['product', 'item', 'goods', 'merchandise']
    for term in common_terms:
        suggestions.append(f"{product_name} {term}")
    
    return list(set(suggestions))  # Remove duplicates

def format_datetime(dt, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format datetime object to string"""
    if dt is None:
        return ""
    return dt.strftime(format_str)

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def safe_int(value: Any, default: int = 0) -> int:
    """Safely convert value to integer"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def safe_float(value: Any, default: float = 0.0) -> float:
    """Safely convert value to float"""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default 