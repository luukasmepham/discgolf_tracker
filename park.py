from db import execute_query

def get_parks():
    query = "SELECT name FROM serv.parks"
    parks = execute_query(query)
    return [row[0] for row in parks] if parks else []

def create_park(park_name):
    query = "INSERT INTO serv.parks (name) VALUES (%s)"
    execute_query(query, (park_name,))
    return True
