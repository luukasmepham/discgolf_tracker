from passlib.hash import bcrypt
from db import execute_query

def verify_user(username, password):
    query = "SELECT username, password FROM serv.user WHERE username = %s"
    user = execute_query(query, (username,))
    if user and bcrypt.verify(password, user[0][1]):
        return True
    return False

def create_user(username, password):
    hashed_password = bcrypt.hash(password)
    query = "INSERT INTO serv.user (username, password) VALUES (%s, %s)"
    execute_query(query, (username, hashed_password))
    return True
