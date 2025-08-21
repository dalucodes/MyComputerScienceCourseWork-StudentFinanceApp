import sqlite3
import os 
conn= sqlite3.connect("finance.db")
c=conn.cursor()

c.execute(
    """CREATE TABLE Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL, 
        iterations INTEGER NOT NULL

    )""")
conn.commit()































# c.execute("SELECT sqlite_version();") #checking the version of sql
# print(c.fetchone())# printing the version
