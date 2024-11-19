import bcrypt
import os

salt = bcrypt.gensalt()
p = "password123"
hashP = bcrypt.hashpw(p, salt)
print(salt)
print(hashP)
