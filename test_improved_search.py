#!/usr/bin/env python3
"""
Test script for improved image search functionality
Demonstrates the new multi-engine image search capabilities
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.image_search import ImageSearchService

def test_image_search():
    """Test the improved image search functionality"""
    print("Testing Improved Image Search")
    print("=" * 50)
    
    # Initialize the search service
    search_service = ImageSearchService()
    
    # Test search terms
    test_terms = [
        "iPhone 13 Pro",
        "Sony WH-1000XM4 headphones",
        "Logitech MX Master 3 mouse"
    ]
    
    for term in test_terms:
        print(f"\nSearching for: {term}")
        print("-" * 30)
        
        try:
            # Try Google search first
            print("Trying Google Images...")
            images = search_service.search_images(term, engine='google', max_results=5)
            
            if images:
                print(f"Found {len(images)} images from Google:")
                for i, img in enumerate(images[:3], 1):
                    print(f"  {i}. {img['title']} ({img['source']})")
                    print(f"     URL: {img['url'][:80]}...")
            else:
                print("No images found from Google, trying Bing...")
                images = search_service.search_images(term, engine='bing', max_results=5)
                
                if images:
                    print(f"Found {len(images)} images from Bing:")
                    for i, img in enumerate(images[:3], 1):
                        print(f"  {i}. {img['title']} ({img['source']})")
                        print(f"     URL: {img['url'][:80]}...")
                else:
                    print("No images found from Bing, using fallback...")
                    images = search_service.search_images(term, engine='fallback', max_results=5)
                    
                    if images:
                        print(f"Found {len(images)} demo images:")
                        for i, img in enumerate(images[:3], 1):
                            print(f"  {i}. {img['title']} ({img['source']})")
                            print(f"     URL: {img['url'][:80]}...")
                    else:
                        print("No images found at all!")
                        
        except Exception as e:
            print(f"Error searching for '{term}': {e}")
            print("Using fallback...")
            try:
                images = search_service.search_images(term, engine='fallback', max_results=5)
                if images:
                    print(f"Found {len(images)} demo images:")
                    for i, img in enumerate(images[:3], 1):
                        print(f"  {i}. {img['title']} ({img['source']})")
                        print(f"     URL: {img['url'][:80]}...")
            except Exception as e2:
                print(f"Fallback also failed: {e2}")

def test_search_engines():
    """Test different search engines"""
    print("\n\nTesting Different Search Engines")
    print("=" * 50)
    
    search_service = ImageSearchService()
    test_term = "iPhone 13 Pro"
    
    engines = ['google', 'bing', 'duckduckgo', 'fallback']
    
    for engine in engines:
        print(f"\nTesting {engine.upper()} search engine:")
        print("-" * 30)
        
        try:
            images = search_service.search_images(test_term, engine=engine, max_results=3)
            print(f"Found {len(images)} images:")
            
            for i, img in enumerate(images, 1):
                print(f"  {i}. {img['title']} ({img['source']})")
                print(f"     URL: {img['url'][:60]}...")
                
        except Exception as e:
            print(f"Error with {engine}: {e}")

if __name__ == "__main__":
    print("Smart Image Updater - Improved Search Test")
    print("=" * 60)
    print("This script tests the new multi-engine image search functionality.")
    print("It will try to find real product images from various search engines.")
    print("If real search fails, it will fall back to demo images.\n")
    
    try:
        test_image_search()
        test_search_engines()
        
        print("\n" + "=" * 60)
        print("Test completed!")
        print("The improved search now supports:")
        print("- Google Images (real product images)")
        print("- Bing Images (real product images)")
        print("- DuckDuckGo Images (real product images)")
        print("- Picsum Photos (demo fallback)")
        print("\nNote: Real search engines may have rate limits or require API keys")
        print("for production use. This implementation uses web scraping.")
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user.")
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        print("Make sure all dependencies are installed:")
        print("pip install -r requirements.txt") 