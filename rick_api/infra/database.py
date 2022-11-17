from rick_api.config import USER_NAME, USER_PASSWORD
from psycopg2.extras import RealDictCursor
import psycopg2

class Database(): 
    def __init__(self, db="postgres", host="localhost", user=USER_NAME, password=USER_PASSWORD):
        self.conn = psycopg2.connect(dbname=db, host=host, user=user, password=password)
        self.cur = self.conn.cursor(cursor_factory= RealDictCursor)


    def insert(self, table, **columns):

        column_title = []
        values = []
        values_placeholder = []

        for column, value in columns.items():
            column_title.append(column)
            values.append(value)
            values_placeholder.append("%s")
        
        delimiter = ','
        insert_query = f"INSERT INTO {table}({delimiter.join(column_title)}) VALUES({delimiter.join(values_placeholder)})"

        try:
            self.cur.execute(insert_query, values)
            self.conn.commit()
        except psycopg2.DatabaseError as e:
            #si ça rate on annule le commit et on passe au suivant
            self.conn.rollback()
            print(e)

    def get(self, what, where, join = True, table_join = "", join_key1 = "", join_key2 = ""):
        
        if not join:
            select_query = f"SELECT {what} FROM {where}"
        else:
            select_query = f"SELECT {what} FROM {where} INNER JOIN {table_join} ON {join_key1} = {join_key2}"
        
        ## To prevent SQL Injections
        select_query.replace("--", "")
        
        try:
            data = self.cur.execute(select_query)
            return data
        
        except psycopg2.DatabaseError as e:
            print(e)
            pass

    def close(self):
        self.cur.close()
        self.conn.close()
