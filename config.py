import os

# Be sure to first setup the environment variables in your machine.
class Config:

    # Parameters for where the server will be run.
    API_IP = os.environ.get('API_IP')
    API_PORT = os.environ.get('API_PORT')

    # For hashing
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Make sure that the MySQL server is running and the parameters are correct.
    DB_HOST = os.environ.get('DB_HOST')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
