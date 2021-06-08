import json
from dotenv.main import load_dotenv
import flask
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

@app.route('/add/<string:username>', methods=['POST'])
def add_user(username):
  print(username)
  try:
    cur = mysql.connection.cursor()
    cur.execute( "INSERT INTO users (name) VALUES (%s)", [username])
    mysql.connection.commit()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
  except TypeError as e:
    return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
  finally:
    cur.close()

@app.route('/users', methods=['GET'])
def get_users():
  try:
    cur = mysql.connection.cursor()
    cur.execute("SELECT name FROM users")
    tuples = cur.fetchall()
    return flask.jsonify(tuples)
  except TypeError as e:
    return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
  finally:
    cur.close()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)