from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from product import Product
from create_db import add_db
import os


#Init app
app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'mysql://root@127.0.0.1:3306/PRODUCT'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/", methods = ['GET'])
def home():
  return jsonify(msg="Hello world!")

#Add product
@app.route("/product", methods = ['POST'])
def product_info():
  name = request.json['name']
  price = request.json['price']
  qty = request.json['qty']
  #new_product = Product(name, price, qty)


def db_object():
    database = add_db("PRODUCT")
    database.execute_query('CREATE DATABASE PRODUCT')
    sql_statement = "CREATE TABLE products (name VARCHAR(255) NOT NULL, price INT NOT NULL, qty INT NOT NULL, PRIMARY KEY (name))"  
    database.execute_query(sql_statement)
    return 

#Run Server
if __name__ == '__main__':
    db_object()
    new_product = Product("hello", 1,1)
    app.run(debug=True)