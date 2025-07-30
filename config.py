import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration class"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///database/products.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Image processing settings
    IMAGE_SIZE = (500, 500)  # Square format
    UPLOAD_FOLDER = 'uploads/products'
    TEMP_FOLDER = 'uploads/temp'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    
    # Image search settings
    SEARCH_ENGINE = 'google'  # Options: google, bing, duckduckgo
    MAX_SEARCH_RESULTS = 20
    SEARCH_TIMEOUT = 30  # seconds
    
    # Web scraping settings
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    REQUEST_TIMEOUT = 10  # seconds
    MAX_RETRIES = 3

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
} 