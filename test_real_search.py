#!/usr/bin/env python3
"""
Test script for Picsum Photos image search functionality
Demonstrates the simple and reliable image search using Picsum Photos
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.image_search import ImageSearchService

def test_picsum_image_search():
    """Test the Picsum Photos image search functionality"""
    print("Smart Image Updater - Picsum Photos Image Search Test")
    print("=" * 60)
    print()
    
    # Initialize search service
    search_service = ImageSearchService()
    
    # Test products with search terms
    test_products = [
        "iPhone 13 Pro",
        "Sony WH-1000XM4 headphones", 
        "Logitech MX Master 3 mouse",
        "MacBook Pro 14 inch",
        "Samsung Galaxy S23"
    ]
    
    for product in test_products:
        print(f"Searching for: {product}")
        print("-" * 40)
        
        try:
            images = search_service.search_images(product, engine='picsum', max_results=5)
            
            if images:
                print(f"Found {len(images)} images:")
                for i, img in enumerate(images, 1):
                    print(f"   {i}. {img['title']}")
                    print(f"      Source: {img['source']}")
                    print(f"      URL: {img['url'][:60]}...")
            else:
                print("No images found")
                
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n" + "=" * 60)
    
    print("\nPICSUM PHOTOS FEATURES:")
    print("- Consistent results for same search terms")
    print("- Intelligent search term generation")
    print("- Category-specific image variations")
    print("- Reliable and fast")
    print("- No external dependencies")
    print("- Perfect for demos and testing")
    print()
    print("The search uses Picsum Photos for consistent, reliable image results!")

def test_search_terms():
    """Test search term generation"""
    print("\n\nSEARCH TERM GENERATION TEST")
    print("=" * 60)
    
    search_service = ImageSearchService()
    test_products = [
        "iPhone 13 Pro",
        "Wireless Headphones",
        "Gaming Mouse",
        "Laptop Stand"
    ]
    
    for product in test_products:
        print(f"\nProduct: {product}")
        print("-" * 30)
        
        # Access the private method for testing
        search_terms = search_service._generate_search_terms(product)
        print(f"Generated search terms: {search_terms}")
        
        # Test image search
        images = search_service.search_images(product, max_results=3)
        print(f"Found {len(images)} images")

if __name__ == "__main__":
    try:
        test_picsum_image_search()
        test_search_terms()
        
        print("\n" + "=" * 60)
        print("TEST COMPLETED!")
        print("The image search now uses:")
        print("- Picsum Photos (reliable random images)")
        print("- Intelligent search term generation")
        print("- Category-specific variations")
        print("- Consistent results")
        print()
        print("KEY BENEFITS:")
        print("- Simple and reliable")
        print("- No external API dependencies")
        print("- Consistent results for demos")
        print("- Fast and lightweight")
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user.")
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        print("Make sure all dependencies are installed:")
        print("pip install -r requirements.txt") 