from flask import Flask, render_template, request
import csv
import json
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)

    return render_template('items.html', items=data.get('items', []))


@app.route('/products')
def products():
    source = request.args.get('source')
    productid = request.args.get('id')

    errorM = None
    products_list = []

    if source == 'json':
        with open('products.json', 'r') as file:
            data = json.load(file)
        if productid:
            for prod in data:
                if str(prod['id']) == str(productid):
                    products_list.append(prod)
            if not products_list:
                errorM = 'Product not found'
        else:
            products_list = data
    elif source == 'csv':
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            if productid:
                for prod in data:
                    if str(prod['id']) == str(productid):
                        products_list.append(prod)
                if not products_list:
                    errorM = 'Product not found'
            else:
                products_list = data
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            curs = conn.cursor()

            if productid:
                curs.execute(
                    'SELECT id, name, category, price FROM Products WHERE id\
                          = ?', (productid,))
            else:
                curs.execute('SELECT id, name, category, price FROM Products')
            rows = curs.fetchall()

            for row in rows:
                products_list.append(
                    {'id': row[0], 'name': row[1],
                     'category': row[2], 'price': row[3]})
            if not products_list:
                errorM = 'Product not found'
            conn.close()
        except sqlite3.Error:
            errorM = 'Database error'

    else:
        errorM = 'Wrong source'

    return render_template(
        'product_display.html',
        products=products_list,
        error=errorM)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
