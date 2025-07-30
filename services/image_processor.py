import requests
import os
from PIL import Image
from io import BytesIO
import hashlib
from typing import Tuple, Optional
from urllib.parse import urlparse
import time

class ImageProcessor:
    """Service for processing and saving images"""
    
    def __init__(self, upload_folder: str = 'uploads/products', temp_folder: str = 'uploads/temp'):
        self.upload_folder = upload_folder
        self.temp_folder = temp_folder
        self.image_size = (500, 500)  # Square format
        self.allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
        
        # Create directories if they don't exist
        os.makedirs(self.upload_folder, exist_ok=True)
        os.makedirs(self.temp_folder, exist_ok=True)
    
    def process_and_save_image(self, image_url: str, product_code: str) -> str:
        """
        Download, process, and save an image
        
        Args:
            image_url: URL of the image to download
            product_code: Product code to use in filename
            
        Returns:
            Path to the saved image
        """
        try:
            # Download image
            image_data = self._download_image(image_url)
            if not image_data:
                raise Exception("Failed to download image")
            
            # Process image
            processed_image = self._process_image(image_data)
            if not processed_image:
                raise Exception("Failed to process image")
            
            # Save image
            filename = self._generate_filename(product_code, image_url)
            filepath = os.path.join(self.upload_folder, filename)
            
            processed_image.save(filepath, 'JPEG', quality=85, optimize=True)
            
            return filepath
            
        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")
    
    def _download_image(self, image_url: str) -> Optional[BytesIO]:
        """Download image from URL"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(image_url, headers=headers, timeout=30, stream=True)
            response.raise_for_status()
            
            # Check content type
            content_type = response.headers.get('content-type', '')
            if not content_type.startswith('image/'):
                raise Exception(f"Invalid content type: {content_type}")
            
            # Check file size (max 10MB)
            content_length = response.headers.get('content-length')
            if content_length and int(content_length) > 10 * 1024 * 1024:
                raise Exception("Image file too large")
            
            # Read image data
            image_data = BytesIO()
            for chunk in response.iter_content(chunk_size=8192):
                image_data.write(chunk)
            
            image_data.seek(0)
            return image_data
            
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None
    
    def _process_image(self, image_data: BytesIO) -> Optional[Image.Image]:
        """Process image to square format"""
        try:
            # Open image
            image = Image.open(image_data)
            
            # Convert to RGB if necessary
            if image.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', image.size, (255, 255, 255))
                if image.mode == 'P':
                    image = image.convert('RGBA')
                background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                image = background
            elif image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize to square format
            processed_image = self._resize_to_square(image, self.image_size)
            
            return processed_image
            
        except Exception as e:
            print(f"Error processing image: {e}")
            return None
    
    def _resize_to_square(self, image: Image.Image, size: Tuple[int, int]) -> Image.Image:
        """Resize image to square format with proper cropping"""
        width, height = image.size
        target_width, target_height = size
        
        # Calculate aspect ratio
        aspect_ratio = width / height
        
        if aspect_ratio > 1:  # Landscape
            # Crop to square from center
            crop_size = height
            left = (width - crop_size) // 2
            top = 0
            right = left + crop_size
            bottom = crop_size
            image = image.crop((left, top, right, bottom))
        elif aspect_ratio < 1:  # Portrait
            # Crop to square from center
            crop_size = width
            left = 0
            top = (height - crop_size) // 2
            right = crop_size
            bottom = top + crop_size
            image = image.crop((left, top, right, bottom))
        
        # Resize to target size
        image = image.resize(size, Image.Resampling.LANCZOS)
        
        return image
    
    def _generate_filename(self, product_code: str, image_url: str) -> str:
        """Generate unique filename for the image"""
        # Get file extension from URL
        parsed_url = urlparse(image_url)
        path = parsed_url.path.lower()
        
        # Determine extension
        extension = '.jpg'  # Default
        for ext in self.allowed_extensions:
            if path.endswith(ext):
                extension = ext
                break
        
        # Generate hash for uniqueness
        timestamp = str(int(time.time()))
        hash_string = hashlib.md5(f"{product_code}{timestamp}".encode()).hexdigest()[:8]
        
        # Clean product code for filename
        clean_code = "".join(c for c in product_code if c.isalnum() or c in ('-', '_')).rstrip()
        
        return f"{clean_code}_{hash_string}{extension}"
    
    def validate_image(self, image_path: str) -> bool:
        """Validate if an image file is valid"""
        try:
            with Image.open(image_path) as img:
                img.verify()
            return True
        except Exception:
            return False
    
    def get_image_info(self, image_path: str) -> dict:
        """Get information about an image file"""
        try:
            with Image.open(image_path) as img:
                return {
                    'size': img.size,
                    'mode': img.mode,
                    'format': img.format,
                    'file_size': os.path.getsize(image_path)
                }
        except Exception as e:
            return {'error': str(e)}
    
    def cleanup_temp_files(self):
        """Clean up temporary files"""
        try:
            for filename in os.listdir(self.temp_folder):
                filepath = os.path.join(self.temp_folder, filename)
                if os.path.isfile(filepath):
                    # Remove files older than 1 hour
                    if time.time() - os.path.getmtime(filepath) > 3600:
                        os.remove(filepath)
        except Exception as e:
            print(f"Error cleaning up temp files: {e}") 