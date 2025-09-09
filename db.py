import sqlite3
import os 
import security
conn= sqlite3.connect("finance.db")
c=conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL, 
        iterations INTEGER NOT NULL

    )""")
conn.commit()
c.execute("SELECT * FROM Users")
# print(c.fetchall())


# c.execute(
#     """INSERT INTO Users (name, email, password_hash, salt, iterations)
#      VALUES("Alice", "alice@example.com", "hash123", "salt123", 100000)"""
 
# )

# conn.commit()

def get_user_email(email):
    email=email.strip().lower()
    query = "SELECT id, name, email, password_hash, salt, iterations FROM Users WHERE email = ?"
    c.execute(query, (email,))
    row= c.fetchone()
    if row is None:
        return None
    return {
        "id": row[0],
        "name": row[1],
        "email": row[2],
        "password_hash": row[3],
        "salt": row[4],
        "iterations": row[5]
    }


def create_user_email(name, email, password):
    name_clean = name.strip()
    email_clean = email.strip().lower()
    record = security.hash_password(password)
    if record is None:
        print("Failed to hash password.")
        return None
    try:
        query = "INSERT INTO Users (name, email, password_hash, salt, iterations)VALUES (?, ?, ?, ?, ?)"
        c.execute(query, (
            name_clean,
            email_clean,
            record["hash"],
            record["salt"],
            record["iterations"]
        ))
        conn.commit()
        return c.lastrowid  
    except TypeError as err:
        print("Error: That email is already in use.")
        return None

























# c.execute("SELECT sqlite_version();") #checking the version of sql
# print(c.fetchone())# printing the version
