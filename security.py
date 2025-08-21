
import os 
import hashlib 
import hmac 
import time
from getpass import getpass

ITERATIONS= 100000
def hash_password(password):
    if password is None or password == b"":
        print("Password cannot be empty.")
        return None
    salt =os.urandom(16)
    hashed= hashlib.pbkdf2_hmac("sha256",password,salt,ITERATIONS)
      #Db doesn't like raw binary in text fields
        #salt and hashed are bytes objects(basically raw bnary)
    return{

    "salt":salt.hex(),
    "hash": hashed.hex(),
    "iterations": ITERATIONS
    }
    
def password_verification(password,record):
    try:
        """Changing salt and hash back to binary"""
        salt_bytes = bytes.fromhex(record["salt"])
        hash_bytes = bytes.fromhex(record["hash"])
        real_password = hashlib.pbkdf2_hmac("sha256",password, salt_bytes, record["iterations"])
        if real_password == hash_bytes:
            return True
    except KeyError as err:
        print("Record is missing a field:", err)
        return False
    except TypeError:
        print("Types are wrong (did you forget .encode() on the password?)")
        return False
    except ValueError as err:
        print("Bad value (check iterations are a positive integer):", err)
        return False
    except Exception as err:
        print("Error during verification:", err)
        return False
    
def read_password(prompt):
    txt = getpass(prompt)   
    txt = txt.strip()      
    if txt == "":
        print("Password cannot be empty.")
        return None
    return txt.encode()   

#signup
user_input = None
while user_input is None:
    user_input = read_password("Create a password: ")

user_record = hash_password(user_input)

#restricted login after 5 attempts 
MAX_ATTEMPTS =5
LOCK_SECONDS = 15
attempts = 0

while True:
    if attempts >= MAX_ATTEMPTS:
        print(f"Too many attempts. Please wait for {LOCK_SECONDS} seconds...")
        time.sleep(LOCK_SECONDS)
        attempts =0
    login_txt = getpass("Enter your password:").strip()
    if login_txt =="":
        print("Password can not be empty.")
        continue
    login_txt =login_txt.encode()
    if password_verification(login_txt, user_record):
        print("Acess granted")
        break
    else:
        attempts +=1
        remaining =MAX_ATTEMPTS -attempts
        if remaining >0:
            print(f"Acess Denied. {remaining} attempts left.")
