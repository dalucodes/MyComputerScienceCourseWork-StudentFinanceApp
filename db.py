import sqlite3
import os 
import security
import expenseTracking
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
c.execute(
    """CREATE TABLE IF NOT EXISTS Expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        amount REAL NOT NULL,
        category TEXT NOT NULL ,
        merchant TEXT,
        notes TEXT, 
        date TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES Users(id)

    )""")
conn.commit()
# c.execute("SELECT * FROM Users")
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

def verify_user(email, password):
    user_record= get_user_email(email)
    if user_record is None:
        print("No account found for that email")
        return False
    passwordToByte= password.encode()
    record ={
       " salt" :user_record["salt"],
        "hash": user_record["password_hash"],     
        "iterations": user_record["iterations"] 
    }
    if security.password_verification(passwordToByte,record):
        print("Access granted")
        return True
    else:
        print("Access denied")
        return False
    
def save_expenses(user_id, expense_record):
    query= """
        INSERT INTO Expenses(amount,category,merchant,notes,date,user_id)
        VALUES(?,?,?,?,?,?)
    """
    c.execute(query,(
        expense_record["amount"],
        expense_record["category"],
        expense_record["merchant"],
        expense_record["notes"],
        expense_record["date"].isoformat(),
        user_id
    ))
    conn.commit()
    return c.lastrowid

def get_expenses(user_id):
    query= "SELECT id, amount, category,merchant,notes,date FROM Expenses WHERE user_id =?"
    c.execute(query,(user_id,))
    rows = c.fetchall()
    expenses =[]
    for row in rows:
        expenses.append({
            "id":row[0],
            "amount":row[1],
            "category":row[2],
            "merchant":row[3],
            "notes":row[4],
            "date":row[5]
        })
    return expenses






















# c.execute("SELECT sqlite_version();") #checking the version of sql
# print(c.fetchone())# printing the version
# 15243566