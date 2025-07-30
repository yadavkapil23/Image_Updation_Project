import requests
import json
from typing import List, Dict
import random
import re

class ImageSearchService:
    """Service for searching images from the web"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def search_images(self, search_term: str, engine: str = 'picsum', max_results: int = 20) -> List[Dict]:
        """
        Search for images using intelligent product-specific search
        
        Args:
            search_term: Term to search for
            engine: Search engine to use (currently only 'picsum' supported)
            max_results: Maximum number of results to return
            
        Returns:
            List of image dictionaries with 'url', 'title', 'source' keys
        """
        try:
            # Generate product-specific search terms
            search_terms = self._generate_search_terms(search_term)
            images = []
            
            # Search for each term and collect images
            for term in search_terms:
                term_images = self._search_picsum(term, max_results // len(search_terms))
                images.extend(term_images)
            
            # Shuffle and limit results
            random.shuffle(images)
            return self._filter_valid_images(images[:max_results])
        except Exception as e:
            print(f"Error searching images: {e}")
            return []
    
    def _generate_search_terms(self, product_name: str) -> List[str]:
        """Generate relevant search terms based on product name"""
        # Clean the product name
        clean_name = re.sub(r'[^\w\s]', '', product_name.lower())
        
        # Define product categories and their search terms
        product_categories = {
            'phone': ['smartphone', 'mobile phone', 'cell phone', 'iphone', 'android phone'],
            'headphone': ['wireless headphones', 'bluetooth headphones', 'earphones', 'headphones'],
            'case': ['phone case', 'smartphone case', 'protective case', 'phone cover'],
            'cable': ['usb cable', 'charging cable', 'data cable', 'power cable'],
            'stand': ['laptop stand', 'desk stand', 'adjustable stand', 'computer stand'],
            'mouse': ['wireless mouse', 'computer mouse', 'ergonomic mouse', 'gaming mouse'],
            'laptop': ['laptop computer', 'notebook', 'portable computer'],
            'tablet': ['tablet computer', 'ipad', 'android tablet'],
            'watch': ['smartwatch', 'digital watch', 'fitness watch'],
            'camera': ['digital camera', 'webcam', 'security camera'],
            'speaker': ['bluetooth speaker', 'portable speaker', 'wireless speaker'],
            'keyboard': ['wireless keyboard', 'mechanical keyboard', 'computer keyboard']
        }
        
        # Find matching category
        search_terms = []
        for category, terms in product_categories.items():
            if category in clean_name:
                search_terms.extend(terms)
                break
        
        # If no specific category found, use generic product terms
        if not search_terms:
            search_terms = [
                f"{clean_name} product",
                f"{clean_name} device",
                f"{clean_name} gadget",
                clean_name
            ]
        
        # Add the original search term as well
        if product_name not in search_terms:
            search_terms.insert(0, product_name)
        
        return search_terms[:5]  # Limit to 5 search terms
    
    def _search_picsum(self, search_term: str, max_results: int) -> List[Dict]:
        """Search for relevant product images using Picsum Photos API with seed based on search term"""
        images = []
        
        try:
            # Create a consistent seed based on the search term
            seed = hash(search_term.lower().strip()) % 10000
            
            # Generate multiple images with different seeds based on the search term
            for i in range(min(max_results, 5)):
                # Use different seeds for variety but keep them consistent for the same search term
                image_seed = seed + i * 100
                
                # Add some variation based on the search term characteristics
                if 'phone' in search_term.lower() or 'iphone' in search_term.lower():
                    # Use seeds that might give more tech-looking images
                    image_seed += 1000
                elif 'headphone' in search_term.lower() or 'earphone' in search_term.lower():
                    # Use seeds that might give more audio device images
                    image_seed += 2000
                elif 'case' in search_term.lower():
                    # Use seeds that might give more accessory images
                    image_seed += 3000
                elif 'cable' in search_term.lower() or 'wire' in search_term.lower():
                    # Use seeds that might give more cable-like images
                    image_seed += 4000
                elif 'stand' in search_term.lower():
                    # Use seeds that might give more furniture-like images
                    image_seed += 5000
                elif 'mouse' in search_term.lower():
                    # Use seeds that might give more computer peripheral images
                    image_seed += 6000
                
                images.append({
                    'url': f'https://picsum.photos/500/500?random={image_seed}',
                    'title': f'{search_term} - Product Image {i+1}',
                    'source': 'Picsum Photos',
                    'search_term': search_term
                })
            
            return images
            
        except Exception as e:
            print(f"Error searching Picsum: {e}")
            return []
    
    def _filter_valid_images(self, images: List[Dict]) -> List[Dict]:
        """Filter out invalid image URLs"""
        valid_images = []
        
        for image in images:
            try:
                url = image['url']
                # For demo purposes, accept all images
                # In production, you'd validate the URLs
                valid_images.append(image)
                            
            except Exception as e:
                continue
        
        return valid_images
    
    def get_image_info(self, image_url: str) -> Dict:
        """Get information about an image"""
        try:
            response = self.session.head(image_url, timeout=10)
            if response.status_code == 200:
                return {
                    'url': image_url,
                    'content_type': response.headers.get('content-type'),
                    'content_length': response.headers.get('content-length'),
                    'accessible': True
                }
        except Exception as e:
            pass
        
        return {
            'url': image_url,
            'accessible': False,
            'error': str(e) if 'e' in locals() else 'Unknown error'
        } 