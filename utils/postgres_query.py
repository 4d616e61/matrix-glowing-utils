import os
import subprocess
import psycopg2


db_conn = None

def query(command : str):
    cur = db_conn.cursor()
    cur.execute(command)
    res = cur.fetchall()
    return res

def init(db_name : str):
    global db_conn
    db_conn = psycopg2.connect(database=db_name,host="localhost", user="postgres", port=5432)
    return db_conn

