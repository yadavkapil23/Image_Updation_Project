#!/usr/bin/env python3
"""
Run script for Smart Image Updater
Simple script to start the Flask application
"""

import os
import sys
from app import app, init_db

def main():
    """Main function to run the application"""
    print("Starting Smart Image Updater...")
    print("=" * 50)
    
    # Check if database exists, if not initialize it
    db_path = 'database/products.db'
    if not os.path.exists(db_path):
        print("Initializing database...")
        init_db()
        print("Database initialized successfully!")
    else:
        print("Database already exists!")
    
    print("\nStarting web server...")
    print("Application will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\nServer stopped. Goodbye!")
    except Exception as e:
        print(f"\nError starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 