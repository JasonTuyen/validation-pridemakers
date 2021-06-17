from flask import Flask
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

app = Flask(__name__) # application 'app' is object of class 'Flask'

# import files
from routes import *

if __name__ == '__main__':
    # '0.0.0.0' = 127.0.0.1 i.e. localhost
    # port = 5000 : we can modify it for localhost
    app.run(host='0.0.0.0', port=5000, debug=True) # local webserver : app.run()

