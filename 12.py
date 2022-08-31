"""
13. Write a Python program to create a backup of a SQLite database. 


"""


import sqlite3
import io
conn = sqlite3.connect('mydatabase.db')
with io.open('clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)
print('Backup performed successfully.')
print('Saved as mydatabase_dump.sql')
conn.close()
