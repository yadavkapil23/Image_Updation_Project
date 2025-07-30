from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create SQLAlchemy instance
db = SQLAlchemy()

class Product(db.Model):
    """Product model for storing product information"""
    
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    image_path = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, name, code, image_path=None):
        self.name = name
        self.code = code
        self.image_path = image_path
    
    def __repr__(self):
        return f'<Product {self.name} ({self.code})>'
    
    def to_dict(self):
        """Convert product to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'image_path': self.image_path,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @property
    def has_image(self):
        """Check if product has an image"""
        return bool(self.image_path) 