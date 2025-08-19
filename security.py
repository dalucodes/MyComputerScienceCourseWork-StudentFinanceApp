"""making a salt
"""
import os 
salt =os.urandom(16)
print("salt:", salt)
print("Saltlength:", len(salt))

"""Hashing a password with a salt"""
import hashlib 
password = b"Hello123"
hashed= hashlib.pbkdf2_hmac("sha256",password,salt,100000)
print("Hashed password:", hashed)
print("Hashed length:", len(hashed))