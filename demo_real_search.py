#!/usr/bin/env python3
"""
Demo script showing Picsum Photos image search functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.image_search import ImageSearchService

def demo_picsum_search():
    """Demonstrate Picsum Photos image search"""
    print("Smart Image Updater - Picsum Photos Image Search Demo")
    print("=" * 60)
    print()
    
    search_service = ImageSearchService()
    test_product = "iPhone 13 Pro"
    
    print(f"Testing search for: {test_product}")
    print("=" * 40)
    
    print("\nPICSUM PHOTOS SEARCH:")
    print("-" * 50)
    
    try:
        images = search_service.search_images(test_product, engine='picsum', max_results=3)
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
    print("PICSUM PHOTOS FEATURES:")
    print("- Consistent results for same search terms")
    print("- Intelligent search term generation")
    print("- Category-specific image variations")
    print("- Reliable and fast")
    print("- No external dependencies")
    print("- Perfect for demos and testing")
    print()
    print("The search uses Picsum Photos for consistent, reliable image results!")

if __name__ == "__main__":
    demo_picsum_search() 