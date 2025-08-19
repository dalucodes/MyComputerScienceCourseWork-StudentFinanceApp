"""making a salt
"""
import os 
salt =os.urandom(16)
# print("salt:", salt)
# print("Saltlength:", len(salt))

"""Hashing a password with a salt"""
import hashlib 
password = b"Hello123"
hashed= hashlib.pbkdf2_hmac("sha256",password,salt,100000)
# print("Hashed password:", hashed)
# print("Hashed length:", len(hashed))
user_record = {
    "salt":salt,
    "hash": hashed,
    "iterations": 100000
}

def password_verification(password,salt,hash, iterations):
    real_password = hashlib.pbkdf2_hmac("sha256", password, salt, iterations)
    if real_password == hash:
        return True
    else:
        return False 
    
print(password_verification(password,user_record["salt"],user_record["hash"],user_record["iterations"]))