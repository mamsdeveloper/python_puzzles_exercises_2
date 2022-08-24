"""
6. Write a Python program to insert a list of records into a given SQLite table. 


"""


import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        conn = sqlite3.connect('mydatabase.db')
        return conn
    except Error:
        print(Error)


def sql_table(conn, rows):
    cursorObj = conn.cursor()
# Create the table
    cursorObj.execute(
        "CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
    sqlite_insert_query = """INSERT INTO salesman
                          (salesman_id, name, city, commission) 
                          VALUES (?, ?, ?, ?);"""
    cursorObj.executemany(sqlite_insert_query, rows)
    conn.commit()
    print("Number of records after inserting rows:")
    cursor = cursorObj.execute('select * from salesman;')
    print(len(cursor.fetchall()))


# Insert records
rows = [(5001, 'James Hoog', 'New York', 0.15),
        (5002, 'Nail Knite', 'Paris', 0.25),
        (5003, 'Pit Alex', 'London', 0.15),
        (5004, 'Mc Lyon', 'Paris', 0.35),
        (5005, 'Paul Adam', 'Rome', 0.45)]

sqllite_conn = sql_connection()
sql_table(sqllite_conn, rows)

if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
