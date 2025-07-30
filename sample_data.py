#!/usr/bin/env python3
"""
Sample data script for Smart Image Updater
Adds sample products to the database for testing
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, init_db
from models.product import Product, db

def add_sample_products():
    """Add sample products to the database"""
    
    sample_products = [
        {
            'name': 'Wireless Bluetooth Headphones',
            'code': 'WH-001',
            'image_path': None
        },
        {
            'name': 'Smartphone Case - Black',
            'code': 'SC-001',
            'image_path': None
        },
        {
            'name': 'USB-C Charging Cable',
            'code': 'UC-001',
            'image_path': None
        },
        {
            'name': 'Laptop Stand - Adjustable',
            'code': 'LS-001',
            'image_path': None
        },
        {
            'name': 'Wireless Mouse - Ergonomic',
            'code': 'WM-001',
            'image_path': None
        },
        {
            'name': 'Mechanical Keyboard - RGB',
            'code': 'MK-001',
            'image_path': None
        },
        {
            'name': 'Monitor Stand - Dual',
            'code': 'MS-001',
            'image_path': None
        },
        {
            'name': 'Webcam - HD 1080p',
            'code': 'WC-001',
            'image_path': None
        },
        {
            'name': 'Microphone - USB Condenser',
            'code': 'MC-001',
            'image_path': None
        },
        {
            'name': 'Gaming Mouse Pad - Large',
            'code': 'MP-001',
            'image_path': None
        }
    ]
    
    with app.app_context():
        # Check if products already exist
        existing_count = Product.query.count()
        if existing_count > 0:
            print(f"Database already contains {existing_count} products.")
            response = input("Do you want to add sample products anyway? (y/N): ")
            if response.lower() != 'y':
                print("Sample data not added.")
                return
        
        # Add sample products (check for duplicates)
        added_count = 0
        for product_data in sample_products:
            # Check if product with this code already exists
            existing_product = Product.query.filter_by(code=product_data['code']).first()
            if existing_product:
                print(f"Product with code {product_data['code']} already exists, skipping...")
                continue
            
            product = Product(**product_data)
            db.session.add(product)
            added_count += 1
        
        db.session.commit()
        print(f"Added {added_count} new sample products to the database.")
        
        if added_count > 0:
            print("\nNew sample products added:")
            for product_data in sample_products:
                existing_product = Product.query.filter_by(code=product_data['code']).first()
                if existing_product:
                    print(f"- {product_data['name']} ({product_data['code']}) - Already existed")
                else:
                    print(f"- {product_data['name']} ({product_data['code']}) - Added")

if __name__ == '__main__':
    print("Smart Image Updater - Sample Data Generator")
    print("=" * 50)
    
    # Add sample products (database is already initialized in app.py)
    add_sample_products()
    
    print("\nSample data generation complete!")
    print("You can now run the application with: python app.py") 