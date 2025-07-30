#!/usr/bin/env python3
"""
Test the improved image search
"""

from services.image_search import ImageSearchService

def test_relevant_search():
    print("Testing Improved Image Search")
    print("=" * 40)
    
    search = ImageSearchService()
    
    # Test with product-specific terms
    test_terms = [
        "headphones",
        "laptop stand", 
        "smartphone case"
    ]
    
    for term in test_terms:
        print(f"\nSearching for: '{term}'")
        print("-" * 30)
        
        images = search.search_images(term, max_results=3)
        print(f"Found {len(images)} images:")
        
        for i, img in enumerate(images, 1):
            print(f"  {i}. {img['title']}")
            print(f"     URL: {img['url']}")
            print(f"     Source: {img['source']}")
            print()

if __name__ == '__main__':
    test_relevant_search() 