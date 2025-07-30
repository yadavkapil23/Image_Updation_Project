# Smart Image Updater for E-Commerce Catalog

A Flask-based web application that automatically fetches product images from the internet, converts them to square format, and updates your product database.

## Features

- **Product Management**: Add, view, and manage products with unique codes
- **Smart Image Search**: Automatically search Google, Bing, and DuckDuckGo for real product images
- **Image Preview**: Preview multiple image options before selection
- **Image Processing**: Convert images to square format (500x500px) with intelligent cropping
- **Local Storage**: Save images locally with organized file structure
- **Database Integration**: Update product records with new image paths
- **Modern UI**: Clean, responsive interface built with Bootstrap 5

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite (file-based, no setup required)
- **Image Processing**: Pillow (PIL)
- **Web Scraping**: BeautifulSoup4, Selenium, Requests
- **Frontend**: Bootstrap 5, Font Awesome
- **Forms**: Flask-WTF with validation

## Project Structure

```
Weazy_PROJECT/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .env                           # Environment variables (create this)
├── .gitignore                     # Git ignore file
│
├── models/                         # Database models
│   ├── __init__.py
│   └── product.py                 # Product model
│
├── services/                       # Business logic
│   ├── __init__.py
│   ├── product_service.py         # Product management
│   ├── image_search.py            # Image search functionality
│   └── image_processor.py         # Image processing
│
├── utils/                          # Utility functions
│   ├── __init__.py
│   └── helpers.py                 # Helper functions
│
├── static/                         # Static files
│   ├── css/
│   │   └── style.css              # Custom styles
│   ├── js/
│   │   └── main.js                # JavaScript functionality
│   └── images/
│       └── placeholder.png        # Placeholder image
│
├── templates/                      # HTML templates
│   ├── base.html                  # Base template
│   ├── index.html                 # Home page
│   └── products/
│       ├── list.html              # Product list
│       ├── add.html               # Add product
│       ├── search.html            # Image search
│       └── preview.html           # Image preview
│
├── uploads/                        # Uploaded images
│   ├── products/                  # Processed product images
│   └── temp/                      # Temporary files
│
└── database/                       # Database files
    └── products.db                # SQLite database
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd Weazy_PROJECT
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv project-venv
   
   # On Windows
   project-venv\Scripts\activate
   
   # On macOS/Linux
   source project-venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file**
   ```bash
   # Create .env file with your settings
   echo "SECRET_KEY=your-secret-key-here" > .env
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📖 Usage Guide

### 1. Adding Products

1. Click "Add Product" in the navigation
2. Enter product name and unique code
3. Click "Add Product" to save

### 2. Finding Images

1. Go to "All Products" or "Missing Images"
2. Click "Find Images" on any product without an image
3. Enter search terms (product name, code, or keywords)
4. Click "Search Images"

### 3. Selecting and Updating Images

1. Browse through the found images
2. Click on an image to select it
3. Click "Update Product Image" to save
4. The image will be processed and saved locally

### 4. Managing Products

- View all products on the main products page
- See which products have images and which don't
- Search for images for products without them
- View product details and image status

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///database/products.db
```

### Image Processing Settings

Modify `config.py` to adjust:

- Image size (default: 500x500px)
- Upload folder paths
- Allowed file extensions
- Search engine preferences

## 🔧 Customization

### Adding New Search Engines

1. Edit `services/image_search.py`
2. Add new search method to `search_engines` dictionary
3. Implement the search function

### Changing Image Processing

1. Modify `services/image_processor.py`
2. Adjust image size, quality, or format
3. Update cropping logic if needed

### Styling Changes

1. Edit `static/css/style.css`
2. Modify Bootstrap classes in templates
3. Add custom JavaScript in `static/js/main.js`

## Troubleshooting

### Common Issues

1. **Images not loading**
   - Check internet connection
   - Verify search engine accessibility
   - Check firewall settings

2. **Database errors**
   - Ensure database directory exists
   - Check file permissions
   - Delete and recreate database if corrupted

3. **Image processing errors**
   - Verify Pillow installation
   - Check upload directory permissions
   - Ensure sufficient disk space

### Debug Mode

Run with debug mode for detailed error messages:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

## Features in Detail

### Image Search

- **Multiple Engines**: Google, Bing, DuckDuckGo
- **Smart Filtering**: Validates image URLs and formats
- **Error Handling**: Graceful fallbacks and retries
- **Rate Limiting**: Respects search engine limits

### Image Processing

- **Square Cropping**: Intelligent center-based cropping
- **Format Conversion**: Converts to JPEG with optimization
- **Quality Control**: Validates image integrity
- **File Management**: Organized storage with unique names

### Database Management

- **SQLite**: Lightweight, no setup required
- **Product Tracking**: Full CRUD operations
- **Image Paths**: Automatic path management
- **Timestamps**: Creation and update tracking

## 🔒 Security Considerations

- **Input Validation**: All user inputs are validated
- **File Upload Security**: Restricted file types and sizes
- **SQL Injection Protection**: Uses SQLAlchemy ORM
- **XSS Prevention**: Template escaping enabled

## 📈 Performance Optimization

- **Image Caching**: Local storage for faster access
- **Lazy Loading**: Images load on demand
- **Compression**: Optimized image storage
- **Database Indexing**: Efficient queries

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

For issues and questions:

1. Check the troubleshooting section
2. Review the code comments
3. Create an issue in the repository
4. Contact the development team

## Roadmap

- [ ] Batch image processing
- [ ] Cloud storage integration
- [ ] API endpoints
- [ ] User authentication
- [ ] Advanced image filters
- [ ] Export functionality
- [ ] Mobile app

---
 