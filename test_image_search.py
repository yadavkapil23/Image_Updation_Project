#!/usr/bin/env python3
"""
Test script for the improved image search functionality
"""

from services.image_search import ImageSearchService

def test_image_search():
    """Test the improved image search functionality"""
    
    # Initialize the service
    image_search = ImageSearchService()
    
    # Test products from the image
    test_products = [
        "iPhone",
        "Wireless Bluetooth Headphones", 
        "Smartphone Case - Black",
        "USB-C Charging Cable",
        "Laptop Stand - Adjustable",
        "Wireless Mouse - Ergonomic"
    ]
    
    print("Testing Improved Image Search Service")
    print("=" * 50)
    
    for product in test_products:
        print(f"\nSearching for: {product}")
        print("-" * 30)
        
        # Search for images
        images = image_search.search_images(product, max_results=3)
        
        print(f"Found {len(images)} images:")
        for i, image in enumerate(images, 1):
            print(f"  {i}. {image['title']}")
            print(f"     URL: {image['url']}")
            print(f"     Search term used: {image.get('search_term', 'N/A')}")
        
        print()

if __name__ == "__main__":
    test_image_search() 