from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import json
import os

app = Flask(__name__)
app.secret_key = 'ecommerce_secret_key'  # Diperlukan untuk session

# URL API
API_URL = "https://dummyjson.com/products"

# Route utama - menampilkan daftar produk
@app.route('/')
def index():
    # Mengambil data produk dari API
    response = requests.get(API_URL)
    if response.status_code == 200:
        products_data = response.json()
        products = products_data.get('products', [])
        return render_template('index.html', products=products)
    else:
        return render_template('index.html', error="Gagal mengambil data produk")

# Route untuk melihat detail produk
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Mengambil detail produk dari API
    response = requests.get(f"{API_URL}/{product_id}")
    if response.status_code == 200:
        product = response.json()
        return render_template('product_detail.html', product=product)
    else:
        return render_template('index.html', error="Produk tidak ditemukan")

# Route untuk pencarian produk
@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        # Menggunakan API pencarian
        response = requests.get(f"{API_URL}/search?q={query}")
        if response.status_code == 200:
            products_data = response.json()
            products = products_data.get('products', [])
            return render_template('index.html', products=products, query=query)
    return redirect(url_for('index'))

# Route untuk menampilkan produk berdasarkan kategori
@app.route('/category/<category>')
def category(category):
    # Mengambil produk berdasarkan kategori
    response = requests.get(f"{API_URL}/category/{category}")
    if response.status_code == 200:
        products_data = response.json()
        products = products_data.get('products', [])
        return render_template('index.html', products=products, category=category)
    else:
        return redirect(url_for('index'))

# API untuk mendapatkan daftar kategori
@app.route('/api/categories')
def get_categories():
    response = requests.get("https://dummyjson.com/products/categories")
    if response.status_code == 200:
        categories = response.json()
        return jsonify(categories)
    else:
        return jsonify([])
    
# Route untuk menambahkan produk ke keranjang
@app.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    # Mengambil detail produk
    response = requests.get(f"{API_URL}/{product_id}")
    if response.status_code == 200:
        product = response.json()
        
        # Inisialisasi keranjang jika belum ada
        if 'cart' not in session:
            session['cart'] = []
        
        # Cek apakah produk sudah ada di keranjang
        cart = session['cart']
        product_in_cart = False
        
        for item in cart:
            if item['id'] == product_id:
                item['quantity'] += 1
                product_in_cart = True
                break
        
        # Jika produk belum ada di keranjang, tambahkan
        if not product_in_cart:
            cart.append({
                'id': product_id,
                'title': product['title'],
                'price': product['price'],
                'thumbnail': product['thumbnail'],
                'quantity': 1
            })
        
        session['cart'] = cart
        
    return redirect(url_for('view_cart'))

# Route untuk melihat keranjang belanja
@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('view_cart.html', cart=cart, total=total)

# Route untuk menghapus item dari keranjang
@app.route('/remove-from-cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session:
        cart = session['cart']
        session['cart'] = [item for item in cart if item['id'] != product_id]
    return redirect(url_for('view_cart'))

# Route untuk mengubah jumlah item di keranjang
@app.route('/update-cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    if 'cart' in session:
        quantity = int(request.form.get('quantity', 1))
        cart = session['cart']
        
        for item in cart:
            if item['id'] == product_id:
                item['quantity'] = quantity
                break
        
        session['cart'] = cart
    
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)
