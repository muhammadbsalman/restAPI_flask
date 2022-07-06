import pymysql
from create_db import add_db

class Product():
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def add_product(self):
        db = add_db("PRODUCT")
        sql_statement="INSERT INTO products (name, price, qty) VALUES (\"{0}\", {1}, {2})".format(self.name, self.price, self.qty)
        db.execute_query(sql_statement)
