try:
    from mysql.connector import connect, Error
except:
    print("Issue importing mysql.connector")

class Db:
    
    def __init__(self):
        pass
    
    def create(self):
        pass
    
    def connect(self):
        db = None
        
        try:
            with connect(
                host="localhost",
                user="mamp",
                password="123"
            ) as connection:
                print(connection)
        except Error as e:
            print(e)
            
            #cursor = db.cursor()
            
            #cursor.execute("Create DATABASE db")
            
