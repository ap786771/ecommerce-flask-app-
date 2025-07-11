from flask import Blueprint, render_template, session, redirect, url_for, request
from .models import Product
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@main.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    return redirect(url_for('main.index'))

@main.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = Product.query.get(int(pid))
        items.append({'product': product, 'quantity': qty})
        total += product.price * qty
    return render_template('cart.html', items=items, total=total)

@main.route('/checkout')
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')
