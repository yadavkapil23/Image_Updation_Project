from models.product import Product, db
from typing import List, Optional

class ProductService:
    """Service class for product operations"""
    
    def get_all_products(self) -> List[Product]:
        """Get all products"""
        return Product.query.all()
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """Get product by ID"""
        return Product.query.get(product_id)
    
    def get_product_by_code(self, code: str) -> Optional[Product]:
        """Get product by code"""
        return Product.query.filter_by(code=code).first()
    
    def get_products_without_images(self) -> List[Product]:
        """Get products that don't have images"""
        return Product.query.filter(Product.image_path.is_(None)).all()
    
    def add_product(self, product: Product) -> Product:
        """Add a new product"""
        db.session.add(product)
        db.session.commit()
        return product
    
    def update_product(self, product_id: int, **kwargs) -> Optional[Product]:
        """Update product information"""
        product = self.get_product_by_id(product_id)
        if product:
            for key, value in kwargs.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            db.session.commit()
        return product
    
    def update_product_image(self, product_id: int, image_path: str) -> Optional[Product]:
        """Update product image path"""
        return self.update_product(product_id, image_path=image_path)
    
    def delete_product(self, product_id: int) -> bool:
        """Delete a product"""
        product = self.get_product_by_id(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
    
    def search_products(self, search_term: str) -> List[Product]:
        """Search products by name or code"""
        return Product.query.filter(
            (Product.name.contains(search_term)) | 
            (Product.code.contains(search_term))
        ).all()
    
    def get_products_count(self) -> int:
        """Get total number of products"""
        return Product.query.count()
    
    def get_products_with_images_count(self) -> int:
        """Get number of products with images"""
        return Product.query.filter(Product.image_path.isnot(None)).count() 