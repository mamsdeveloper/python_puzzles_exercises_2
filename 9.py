"""
10. Write a Python program to update all the values of a specific column of a given SQLite table. 


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
# Create the table
    cursorObj.execute(
        "CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
# Insert records
    cursorObj.executescript("""
    INSERT INTO salesman VALUES(5001,'James Hoog', 'New York', 0.15);
    INSERT INTO salesman VALUES(5002,'Nail Knite', 'Paris', 0.25);
    INSERT INTO salesman VALUES(5003,'Pit Alex', 'London', 0.15);
    INSERT INTO salesman VALUES(5004,'Mc Lyon', 'Paris', 0.35);
    INSERT INTO salesman VALUES(5005,'Paul Adam', 'Rome', 0.45);
    """)
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)
    print("\nUpdate all commision to .55:")
    sql_update_query = """Update salesman set commission = .55"""
    cursorObj.execute(sql_update_query)
    conn.commit()
    print("Record Updated successfully ")
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("\nAfter updating Agent details:")
    for row in rows:
        print(row)


sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
