#!/usr/bin/env python3
"""
Quick test for image search
"""

from services.image_search import ImageSearchService

def test():
    print("Testing Image Search...")
    
    search = ImageSearchService()
    images = search.search_images("headphones", max_results=3)
    
    print(f"Found {len(images)} images:")
    for i, img in enumerate(images, 1):
        print(f"{i}. {img['title']}")
        print(f"   URL: {img['url']}")
        print()

if __name__ == '__main__':
    test() 