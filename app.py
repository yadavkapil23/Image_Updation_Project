from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", "products.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import models and services
from models.product import Product, db
from services.product_service import ProductService
from services.image_search import ImageSearchService
from services.image_processor import ImageProcessor

# Initialize database with app
def init_db():
    # Ensure database directory exists
    database_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database")
    os.makedirs(database_dir, exist_ok=True)
    
    # Initialize the database with the app
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

# Initialize database first
init_db()

# Initialize services after database is ready
product_service = ProductService()
image_search_service = ImageSearchService()
image_processor = ImageProcessor()

# Forms
class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    code = StringField('Product Code', validators=[DataRequired()])
    submit = SubmitField('Add Product')

class ImageSearchForm(FlaskForm):
    search_term = StringField('Search Term', validators=[DataRequired()])
    submit = SubmitField('Search Images')

# Routes
@app.route('/')
def index():
    """Home page"""
    # Get statistics
    total_products = product_service.get_products_count()
    products_with_images = product_service.get_products_with_images_count()
    products_without_images = total_products - products_with_images
    completion_percentage = round((products_with_images / total_products * 100) if total_products > 0 else 0, 1)
    
    # Get recent products (last 5)
    recent_products = Product.query.order_by(Product.created_at.desc()).limit(5).all()
    
    # Get products needing images (first 5)
    products_needing_images = product_service.get_products_without_images()[:5]
    
    return render_template('index.html', 
                         total_products=total_products,
                         products_with_images=products_with_images,
                         products_without_images=products_without_images,
                         completion_percentage=completion_percentage,
                         recent_products=recent_products,
                         products_needing_images=products_needing_images)

@app.route('/products')
def product_list():
    """List all products"""
    products = product_service.get_all_products()
    return render_template('products/list.html', products=products)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    """Add new product"""
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            code=form.code.data,
            image_path=None
        )
        product_service.add_product(product)
        flash('Product added successfully!', 'success')
        return redirect(url_for('product_list'))
    return render_template('products/add.html', form=form)

@app.route('/products/<int:product_id>/search')
def search_images(product_id):
    """Search for images for a specific product"""
    product = product_service.get_product_by_id(product_id)
    if not product:
        flash('Product not found!', 'error')
        return redirect(url_for('product_list'))
    
    form = ImageSearchForm()
    
    # Pre-populate with product name and perform initial search
    form.search_term.data = product.name
    images = image_search_service.search_images(product.name)
    
    return render_template('products/search.html', 
                         product=product, 
                         form=form, 
                         initial_images=images,
                         search_term=product.name)

@app.route('/products/<int:product_id>/search', methods=['POST'])
def perform_image_search(product_id):
    """Perform image search for a product"""
    form = ImageSearchForm()
    
    # Get search term from form data directly if validation fails
    search_term = form.search_term.data if form.search_term.data else request.form.get('search_term')
    
    # If no search term provided, use the product name as default
    if not search_term:
        product = product_service.get_product_by_id(product_id)
        if product:
            search_term = product.name
        else:
            return jsonify({'error': 'Product not found'}), 404
    
    if search_term:
        product = product_service.get_product_by_id(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        print(f"Searching for: {search_term}")  # Debug print
        images = image_search_service.search_images(search_term)
        print(f"Found {len(images)} images")  # Debug print
        
        return render_template('products/preview.html', 
                             product=product, 
                             images=images, 
                             search_term=search_term)
    else:
        print("No search term provided!")
        print(f"Form errors: {form.errors}")
    
    return redirect(url_for('search_images', product_id=product_id))

@app.route('/products/<int:product_id>/update-image', methods=['POST'])
def update_product_image(product_id):
    """Update product image"""
    data = request.get_json()
    image_url = data.get('image_url')
    
    if not image_url:
        return jsonify({'error': 'Image URL is required'}), 400
    
    product = product_service.get_product_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    try:
        # Download and process image
        image_path = image_processor.process_and_save_image(
            image_url, 
            product.code
        )
        
        # Update product with new image path
        product_service.update_product_image(product_id, image_path)
        
        return jsonify({
            'success': True,
            'message': 'Image updated successfully',
            'image_path': image_path
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products/without-images')
def products_without_images():
    """Show products without images"""
    products = product_service.get_products_without_images()
    return render_template('products/list.html', products=products, title="Products Without Images")

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded images"""
    from flask import send_from_directory
    uploads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
    return send_from_directory(uploads_dir, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 