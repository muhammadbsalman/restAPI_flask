import pymysql

class add_db():
    
    def __init__(self, db=""):
        try:
            self.mydb = pymysql.connect(host='localhost', user='root', password="", database = db, autocommit=True)
        except:
            print("Could not connect to database, please verify login credentials!")

    def execute_query(self, sql_statement):
        self.sql_statement = sql_statement
        print(self.sql_statement)

        try:
            my_cursor = self.mydb.cursor()
            my_cursor.execute(self.sql_statement)
        except Exception as e:
            print(e)
            #print("{0} PROBLEM EXECUTING!".format(self.sql_statement))
        
        return my_cursor