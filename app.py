from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from create_db import add_db
import os


#Init app
app= Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] =\
#        'mysql://root@127.0.0.1:3306'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

#cursor = db.connection.cursor()

@app.route("/", methods = ['GET'])
def home():
  return jsonify(msg="Hello world!")

#Add product
@app.route("/product", methods = ['POST'])
def product():
  name = request.json['name']
  price = request.json['price']
  qty = request.json['qty']

def db_object():
    db_name = "PRODUCT"
    database = add_db(db_name)
    database.execute_query('CREATE DATABASE {0}'.format(db_name))
    return 

#Run Server
if __name__ == '__main__':
    db_object()
    app.run(debug=True)