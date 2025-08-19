
import os 
import hashlib 
import hmac 
import getpass
def hash_password(password):
    salt =os.urandom(16)
    iterations= 100000
    hashed= hashlib.pbkdf2_hmac("sha256",password,salt,iterations)
    dataBase = {
    "salt":salt,
    "hash": hashed,
    "iterations": iterations
    }
    return dataBase
def password_verification(password,record):
    try:
        real_password = hashlib.pbkdf2_hmac("sha256", password, record["salt"], record["iterations"])
        if real_password == record["hash"]:
            return True
    except Exception as e:
        print("Erorr during verification", e)
        return False 
    
user_input= getpass.getpass("Create a password").encode()
user_record = hash_password(user_input)

login_input =getpass.getpass("Enter your password: ").encode()
if password_verification(login_input,user_record) == True:
    print("Acess granted")
else:
    print("access denied")
