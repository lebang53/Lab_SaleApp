from flask import Flask, render_template, request
from __init__ import app
import dao

@app.route('/')
def home():
    categories = dao.load_categories()

    category_id = request.args.get('category_id')
    products = dao.load_products(category_id=category_id)
    return render_template('index.html', categories = categories,
                                        products = products)               

if __name__ == '__main__':
    app.run(debug=True)
