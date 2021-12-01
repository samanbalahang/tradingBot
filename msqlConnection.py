from mysql import connector
class connecting:
    def conn():
        mydb = connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_gram"
        )      
        return mydb
