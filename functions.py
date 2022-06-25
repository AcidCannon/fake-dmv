# helper functions
import sqlite3
import hashlib
import re

def connect(path):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return connection, cursor

def login_check(username, password):
    if re.match("^[A-Za-z0-9_]*$", username) and re.match("^[A-Za-z0-9_]*$", password):
        return True
    return False

# since password is plain text, guess this is redundant, but keep this anyway...
def encrypt(password):
    alg = hashlib.sha256()
    alg.update(password.encode("utf-8"))
    return alg.hexdigest()
