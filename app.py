from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Dummy product data (you can extend this or connect to a real database)
products = [
    {"id": 1, "name": "Laptop", "description": "Description for product 1", "price": 10.99, "image": "product1.jpg"},
    {"id": 2, "name": "I-Phone", "description": "Description for product 2", "price": 20.99, "image": "product2.jpg"},
    {"id": 3, "name": "Gaming Console", "description": "Description for product 3", "price": 30.99, "image": "product3.jpg"}
]

# Route for the homepage showing product listings
@app.route('/')
def index():
    return render_template('index.html', products=products)

# Route for viewing a single product
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return "Product not found", 404
    return render_template('product_detail.html', product=product)

# Route for adding a product to the cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('index'))

# Route for viewing the shopping cart
@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

# Route for clearing the cart
@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
