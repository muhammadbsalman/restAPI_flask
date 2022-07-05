import pymysql

class add_db():
    
    def __init__(self, db_name):

        self.db_name = db_name

        try:
            self.mydb = pymysql.connect(host='localhost', user='root', password="")
        except:
            print("Could not connect to database, please verify login credentials!")
    
    def execute_query(self, sql_statement):
        self.sql_statement = sql_statement
        print(self.sql_statement)

        try:
            my_cursor = self.mydb.cursor()
            my_cursor.execute(sql_statement)
        except:
            print("{0} Database exists!".format(self.db_name))

#Run Server
if __name__ == '__main__':
    db_name = "PRODUCT"
    database = add_db(db_name)
    database.execute_query('CREATE DATABASE {0}'.format(db_name))