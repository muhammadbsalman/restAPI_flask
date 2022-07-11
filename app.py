from flask import Flask, request, jsonify, make_response
from product import Product
from create_db import add_db
import os


#Init app
app= Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return jsonify(msg="Please add your products at /product")

#Add product to db
@app.route("/product", methods = ['GET', 'POST'])
def product_info():
    if request.method == "POST":
        name = request.json['name']
        price = request.json['price']
        qty = request.json['qty']
  
        new_product = Product(name, price, qty)
        new_product.add_product()
  
        resp = jsonify(msg="{0} added to database".format(name))
        return make_response(resp, 200)

    if request.method == "GET":
        list_products = []
        new_list_products = []
        cursor_object = db_object("SELECT * FROM products")
        cursor_object = cursor_object.fetchall()
        for x in cursor_object:
            list_products.append(x)
        for x in list_products:
            result = "name: {0}, price: {1}, qty: {2}".format(x[0], x[1], x[2])
            new_list_products.append(result)
        resp = jsonify(new_list_products)
        return make_response(resp, 200)


#Create Product DB and Table
def db_object(sql_statement):
    database = add_db("PRODUCT")
    cursor_object = database.execute_query(sql_statement)
    return cursor_object

#Run Server
if __name__ == '__main__':
    db_object("CREATE DATABASE PRODUCT")
    db_object("CREATE TABLE products (name VARCHAR(255) NOT NULL, price INT NOT NULL, qty INT NOT NULL, PRIMARY KEY (name))")
    app.run(host='127.0.0.1', port=5000, debug=True)