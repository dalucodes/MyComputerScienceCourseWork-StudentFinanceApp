
import db
import security

# Ask user for sign-up details
name = input("Enter your name: ")
email = input("Enter your email: ")
password = security.read_password("Create a password: ")

if password is not None:
    user_id = db.create_user(name, email, password)
    if user_id:
        print(f"User created! ID: {user_id}")
    else:
        print("❌Failed to create user.")
else:
    print("Signup cancelled (invalid password).")

