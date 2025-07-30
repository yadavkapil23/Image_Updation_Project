#!/usr/bin/env python3
"""
Demo script for improved image search functionality
Shows the difference between old and new search methods
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.image_search import ImageSearchService

def demo_improved_search():
    """Demonstrate the improved image search"""
    print("Smart Image Updater - Improved Search Demo")
    print("=" * 60)
    print()
    
    # Initialize search service
    search_service = ImageSearchService()
    
    # Test product
    test_product = "iPhone 13 Pro"
    print(f"Testing search for: {test_product}")
    print("-" * 40)
    
    # Try different search engines
    engines = [
        ('Google Images', 'google'),
        ('Bing Images', 'bing'), 
        ('DuckDuckGo Images', 'duckduckgo'),
        ('Demo Fallback', 'fallback')
    ]
    
    for engine_name, engine_code in engines:
        print(f"\nTrying {engine_name}...")
        
        try:
            images = search_service.search_images(test_product, engine=engine_code, max_results=3)
            
            if images:
                print(f" Found {len(images)} images:")
                for i, img in enumerate(images, 1):
                    print(f"   {i}. {img['title']}")
                    print(f"      Source: {img['source']}")
                    print(f"      URL: {img['url'][:60]}...")
            else:
                print(" No images found")
                
        except Exception as e:
            print(f" Error: {e}")
    
    print("\n" + "=" * 60)
    print("IMPROVEMENTS SUMMARY:")
    print("Real image search from Google, Bing, DuckDuckGo")
    print("  Intelligent search term generation")
    print("  Duplicate removal")
    print("  URL validation")
    print("  Graceful fallback to demo images")
    print("  Respectful rate limiting")
    print("  Error handling and recovery")
    print()
    print("The search now finds actual product images instead of random photos!")
    print("This makes the application much more useful for real e-commerce use.")

if __name__ == "__main__":
    demo_improved_search() 