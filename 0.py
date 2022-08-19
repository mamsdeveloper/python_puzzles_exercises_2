"""
1. Write a Python program to create a SQLite database and connect with the database and print the version of the SQLite database. 


"""


import sqlite3
try:
    sqlite_Connection = sqlite3.connect('temp.db')
    conn = sqlite_Connection.cursor()
    print("\nDatabase created and connected to SQLite.")
    sqlite_select_Query = "select sqlite_version();"
    conn.execute(sqlite_select_Query)
    record = conn.fetchall()
    print("\nSQLite Database Version is: ", record)
    conn.close()
except sqlite3.Error as error:
    print("\nError while connecting to sqlite", error)
finally:
    if (sqlite_Connection):
        sqlite_Connection.close()
        print("\nThe SQLite connection is closed.")
