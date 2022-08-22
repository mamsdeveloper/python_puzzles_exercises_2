"""
4. Write a Python program to list the tables of given SQLite database file. 


"""


import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        conn = sqlite3.connect('mydatabase.db')
        return conn
    except Error:
        print(Error)


def sql_table(conn):
    cursorObj = conn.cursor()
# Create two tables
    cursorObj.execute(
        "CREATE TABLE agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")
    cursorObj.execute(
        "CREATE TABLE temp_agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")
    print("List of tables:")
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursorObj.fetchall())
    conn.commit()


sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
