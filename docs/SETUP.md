# Smart Image Updater - Setup Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python run.py
```

### 3. Add Sample Data (Optional)
```bash
python sample_data.py
```

### 4. Access the Application
Open your browser and go to: `http://localhost:5000`

## Project Overview

This is a **Smart Image Updater for E-Commerce Catalog** built with Flask. It provides:

- **Product Management**: Add and manage products with unique codes
- **Smart Image Search**: Search multiple engines (Google, Bing, DuckDuckGo)
- **Image Processing**: Convert images to square format (500x500px)
- **Local Storage**: Save images locally with organized structure
- **Modern UI**: Clean, responsive interface with Bootstrap 5

## Key Features

### 1. Product Management
- Add products with name and unique code
- View all products in a clean card layout
- Track which products have images
- Filter products without images

### 2. Image Search
- Search multiple search engines simultaneously
- Preview multiple image options
- Smart filtering of valid image URLs
- Error handling and fallbacks

### 3. Image Processing
- Automatic conversion to square format
- Intelligent center-based cropping
- Quality optimization (JPEG, 85% quality)
- Unique filename generation

### 4. User Interface
- Modern, responsive design
- Interactive image selection
- Real-time statistics and progress
- Intuitive navigation

## File Structure

```
Weazy_PROJECT/
├── app.py                    # Main Flask application
├── run.py                    # Easy startup script
├── sample_data.py            # Add sample products
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── README.md                 # Comprehensive documentation
├── .gitignore               # Git ignore patterns
│
├── models/                   # Database models
│   ├── __init__.py
│   └── product.py           # Product model
│
├── services/                 # Business logic
│   ├── __init__.py
│   ├── product_service.py   # Product operations
│   ├── image_search.py      # Image search engines
│   └── image_processor.py   # Image processing
│
├── utils/                    # Utility functions
│   ├── __init__.py
│   └── helpers.py           # Helper functions
│
├── static/                   # Static files
│   ├── css/style.css        # Custom styles
│   ├── js/main.js           # JavaScript functionality
│   └── images/              # Images and icons
│
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   └── products/            # Product templates
│
├── uploads/                  # Uploaded images
│   ├── products/            # Processed product images
│   └── temp/                # Temporary files
│
└── database/                 # Database files
    └── products.db          # SQLite database
```

## Usage Workflow

### 1. Add Products
1. Click "Add Product" in navigation
2. Enter product name and unique code
3. Save the product

### 2. Find Images
1. Go to "All Products" or "Missing Images"
2. Click "Find Images" on any product
3. Enter search terms
4. Browse results

### 3. Select and Save Images
1. Click on an image to select it
2. Click "Update Product Image"
3. Image is processed and saved

## Configuration

### Environment Variables
Create a `.env` file:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///database/products.db
```

### Customization
- **Image Size**: Modify `IMAGE_SIZE` in `config.py`
- **Search Engines**: Add new engines in `services/image_search.py`
- **Styling**: Edit `static/css/style.css`

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all dependencies are installed
   - Check Python version (3.8+ required)

2. **Database Errors**
   - Delete `database/products.db` and restart
   - Check file permissions

3. **Image Search Issues**
   - Check internet connection
   - Verify search engine accessibility
   - Check firewall settings

4. **Image Processing Errors**
   - Ensure Pillow is installed correctly
   - Check upload directory permissions
   - Verify sufficient disk space

### Debug Mode
The application runs in debug mode by default. For production:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## Development

### Adding Features
1. **New Search Engines**: Add to `services/image_search.py`
2. **Image Processing**: Modify `services/image_processor.py`
3. **UI Changes**: Edit templates and CSS
4. **Database**: Add models in `models/` directory

### Testing
- Test image search with different terms
- Verify image processing quality
- Check responsive design on mobile
- Test error handling scenarios

## Production Deployment

### Requirements
- Python 3.8+
- Web server (nginx, Apache)
- WSGI server (gunicorn, uwsgi)
- SSL certificate

### Security Considerations
- Change default secret key
- Use HTTPS
- Set up proper file permissions
- Configure firewall rules
- Regular backups

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the README.md file
3. Check code comments
4. Create an issue in the repository

---

**Smart Image Updater** - Making e-commerce image management simple and efficient! 