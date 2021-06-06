from typing import OrderedDict
from dotenv.main import load_dotenv
from flask import Flask
from flask_mysqldb import MySQL
from os import getenv
from dotenv import load_dotenv

app = Flask(__name__)

# load .env file
load_dotenv()

print(getenv('MYSQL_HOST'))

app.config['MYSQL_HOST'] = getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = getenv('MYSQL_DB')

mysql = MySQL(app) # Initialize MySQL

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/register', methods=['POST'])
def register():
  return "TBD"

@app.route('/login', methods=['POST'])
def login():
  return "TBD"

@app.route('/signout', methods=['POST'])
def signout():
  return "TBD"

@app.route('/users', methods=['GET'])
def get_users():
  cur = mysql.connection.cursor()
  cur.execute("SELECT name FROM users")
  tuples = cur.fetchall()
  cur.close()
  print(tuples)
  return tuples

if __name__ == '__main__':
  app.run(host='0.0.0.0')