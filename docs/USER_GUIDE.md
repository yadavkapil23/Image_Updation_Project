# Smart Image Updater - User Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Adding Products](#adding-products)
4. [Finding Images](#finding-images)
5. [Image Selection and Processing](#image-selection-and-processing)
6. [Managing Products](#managing-products)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Features](#advanced-features)

---

## Introduction

The Smart Image Updater is a web-based application designed to help e-commerce businesses automatically find and process product images. This guide will walk you through every feature and help you get the most out of the application.

### What This Application Does

- **Automatically searches** the internet for product images
- **Converts images** to square format (500x500 pixels)
- **Stores images locally** with organized file structure
- **Updates your product database** with image paths
- **Provides a modern interface** for easy management

### Key Benefits

- Save hours of manual image searching
- Ensure consistent image dimensions
- Maintain organized product catalogs
- Improve product presentation

---

## Getting Started

### Prerequisites

Before using the application, ensure you have:
- Python 3.8 or higher installed
- Internet connection for image searching
- Web browser (Chrome, Firefox, Safari, or Edge)

### Installation Steps

1. **Download the Project**
   ```bash
   git clone <repository-url>
   cd Weazy_PROJECT
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv project-venv
   
   # On Windows
   project-venv\Scripts\activate
   
   # On macOS/Linux
   source project-venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python run.py
   ```

5. **Access the Application**
   Open your browser and go to: `http://localhost:5000`

### First Time Setup

When you first run the application:
- The database will be automatically created
- Upload directories will be set up
- You'll see a welcome screen with statistics

---

## Adding Products

### Step-by-Step Guide

1. **Navigate to Add Product**
   - Click "Add Product" in the top navigation
   - Or click the green "Add Product" button on the home page

2. **Fill in Product Details**
   - **Product Name**: Enter a descriptive name (e.g., "iPhone 13 Pro")
   - **Product Code**: Enter a unique identifier (e.g., "IPHONE-13-PRO")
   - Click "Add Product" to save

3. **Product Added Successfully**
   - You'll see a success message
   - The product will appear in your product list
   - Initially, it will show "No Image" status

### Best Practices for Product Names

- Use descriptive, specific names
- Include brand names when relevant
- Avoid generic terms like "phone" or "cable"
- Examples:
  - "iPhone 13 Pro Max"
- "Sony WH-1000XM4 Headphones"
- "Logitech MX Master 3 Mouse"
- "Phone"
- "Cable"

### Product Code Guidelines

- Use unique, memorable codes
- Include brand and model information
- Use consistent formatting
- Examples:
  - "IPHONE-13-PRO"
- "SONY-WH1000XM4"
- "LOGITECH-MX-MASTER-3"

---

## Finding Images

### Automatic Search

1. **Access Product List**
   - Click "All Products" in the navigation
   - Or click "View Products" on the home page

2. **Find Products Without Images**
   - Look for products with yellow "No Image" badges
   - Click "Find Images" button on any product

3. **Search Page Features**
   - Search term is pre-filled with product name
   - Multiple search suggestions are provided
   - Initial search results appear automatically

### Manual Search

1. **Enter Search Terms**
   - Use the product name as a starting point
   - Try variations like "product name + product"
   - Use brand names for better results

2. **Search Suggestions**
   - Click suggested search terms for quick searching
   - Try different combinations for better results
   - Use product codes as alternative search terms

### Search Tips

**For Better Results:**
- Use specific product names
- Include brand names
- Add "product" or "item" to search terms
- Try different variations of the name

**Examples:**
- "iPhone 13 Pro" → "iPhone 13 Pro product"
- "Wireless Headphones" → "Sony wireless headphones"
- "Gaming Mouse" → "Logitech gaming mouse"

---

## Image Selection and Processing

### Previewing Images

1. **Browse Search Results**
   - Multiple images are displayed in a grid
   - Each image shows source information
   - Hover over images for details

2. **Select an Image**
   - Click on any image to select it
   - Selected image will be highlighted
   - A preview will appear at the bottom

3. **Image Information**
   - Source: Where the image was found
   - Title: Description of the image
   - Quality: Visual assessment

### Processing and Saving

1. **Update Product Image**
   - Click "Update Product Image" button
   - Confirm your selection
   - Wait for processing to complete

2. **What Happens During Processing**
   - Image is downloaded from the internet
   - Converted to square format (500x500px)
   - Optimized for quality and file size
   - Saved to local storage
   - Database is updated with image path

3. **Success Confirmation**
   - You'll see a success message
   - Product status changes to "Has Image"
   - Image appears in product card

### Image Processing Details

**Square Format Conversion:**
- Images are cropped to square from the center
- Maintains aspect ratio where possible
- Ensures consistent dimensions across all products

**Quality Optimization:**
- JPEG format with 85% quality
- Optimized file sizes
- Maintains visual quality

**File Organization:**
- Images stored in `uploads/products/`
- Unique filenames based on product code
- Automatic cleanup of temporary files

---

## Managing Products

### Viewing All Products

1. **Product List Features**
   - Grid layout showing all products
   - Status indicators (Has Image/No Image)
   - Creation dates
   - Quick action buttons

2. **Product Cards Include**
   - Product name and code
   - Image preview (if available)
   - Status badge
   - Action dropdown menu

### Filtering Products

1. **Products Without Images**
   - Click "Missing Images" in navigation
   - Shows only products needing images
   - Quick access to image search

2. **Recent Products**
   - Home page shows recent additions
   - Quick overview of latest activity

### Product Actions

**Available Actions:**
- **Search Images**: Find images for the product
- **View Image**: Preview current product image
- **Delete**: Remove product from database

**Action Dropdown Menu:**
- Click the three dots (⋮) on any product card
- Select desired action from the menu

### Statistics and Progress

**Dashboard Overview:**
- Total number of products
- Products with images
- Products missing images
- Completion percentage

**Progress Tracking:**
- Visual progress indicators
- Real-time statistics updates
- Completion rate calculation

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Images Not Loading

**Problem**: Search results show no images or broken images

**Solutions:**
- Check your internet connection
- Try different search terms
- Wait a few minutes and try again
- Check if search engines are accessible

#### 2. Image Processing Errors

**Problem**: Images fail to process or save

**Solutions:**
- Ensure sufficient disk space
- Check file permissions on upload directory
- Try a different image from search results
- Restart the application

#### 3. Database Errors

**Problem**: Products not saving or loading

**Solutions:**
- Restart the application
- Check if database file exists
- Ensure proper file permissions
- Delete and recreate database if corrupted

#### 4. Application Won't Start

**Problem**: Error when running the application

**Solutions:**
- Check Python version (3.8+ required)
- Install all dependencies: `pip install -r requirements.txt`
- Check if port 5000 is available
- Try different port: `python app.py --port 5001`

### Debug Information

**Check Application Logs:**
- Look for error messages in terminal
- Check browser console for JavaScript errors
- Verify file permissions on project directory

**Common Error Messages:**
- "Database not found" → Restart application
- "Image download failed" → Check internet connection
- "Permission denied" → Check file permissions

---

## Advanced Features

### Smart Search Intelligence

The application uses intelligent search to find better images:

**Product Category Detection:**
- Automatically detects product types
- Uses category-specific search terms
- Improves search relevance

**Search Term Generation:**
- Creates multiple search variations
- Includes brand names and models
- Combines different search strategies

### Image Quality Control

**Validation Features:**
- Checks image file formats
- Validates image integrity
- Ensures proper dimensions
- Prevents corrupted files

**Processing Options:**
- Automatic format conversion
- Quality optimization
- Size reduction
- Metadata cleanup

### File Management

**Organized Storage:**
- Products stored by code
- Unique filenames
- Automatic cleanup
- Backup considerations

**Upload Structure:**
```
uploads/
├── products/          # Processed product images
└── temp/             # Temporary files
```

### Performance Optimization

**Caching:**
- Local image storage
- Reduced download times
- Faster image loading

**Efficient Processing:**
- Optimized image conversion
- Compressed file sizes
- Quick database updates

---

## Tips for Best Results

### Product Naming

**Do:**
- Use specific, descriptive names
- Include brand and model information
- Be consistent with naming conventions

**Don't:**
- Use generic terms
- Skip important details
- Use inconsistent formatting

### Image Selection

**Choose Images That:**
- Show the product clearly
- Have good lighting and quality
- Match your brand aesthetic
- Are from reliable sources

**Avoid:**
- Blurry or low-quality images
- Images with watermarks
- Inappropriate or irrelevant images
- Copyrighted content

### Search Strategy

**Effective Search Terms:**
- Product name + "product"
- Brand name + model
- Specific features + product type
- Alternative product names

**Example Searches:**
- "iPhone 13 Pro product"
- "Sony WH-1000XM4 headphones"
- "Logitech MX Master 3 mouse"

---

## Support and Resources

### Getting Help

1. **Check This Guide**: Most issues are covered here
2. **Review Error Messages**: Look for specific error details
3. **Check Documentation**: README.md has technical details
4. **Restart Application**: Often resolves temporary issues

### Additional Resources

- **README.md**: Technical documentation
- **Code Comments**: Inline documentation in source code
- **Error Logs**: Check terminal output for details

### Contact Information

For additional support:
- Check the project repository
- Review the troubleshooting section
- Contact the development team

---

## Conclusion

The Smart Image Updater provides a powerful, user-friendly solution for managing product images in e-commerce catalogs. By following this guide, you can efficiently:

- Add and manage products
- Find relevant images automatically
- Process images to consistent formats
- Maintain organized product catalogs

The application is designed to save time and improve the quality of your product presentations. With practice, you'll develop efficient workflows that maximize the benefits of automated image management.

Remember to:
- Use descriptive product names
- Try multiple search terms
- Select high-quality images
- Maintain organized product codes

Happy image updating! 