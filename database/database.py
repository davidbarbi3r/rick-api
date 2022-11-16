from config.config import USER_NAME, USER_PASSWORD
import psycopg2

class Database(): 
    def __init__(self, db="postgres", host="localhost", user=USER_NAME, password=USER_PASSWORD):
        self.conn = psycopg2.connect(dbname=db, host=host, user=user, password=password)
        self.cur = conn.cursor()

    def query(*query):
        cur.execute(query)
    
    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

