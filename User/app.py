import json
from dotenv.main import load_dotenv
import flask
from flask import Flask
from flask_mysqldb import MySQL
from flask_mysqldb import MySQLdb
from datetime import date
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
  return "Fine1"

@app.route('/add/<string:username>', methods=['POST'])
def add_user(username):
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
  print()
  try:
    cur = mysql.connection.cursor()
    cur.execute("SELECT name FROM users")
    tuples = cur.fetchall()
    return flask.jsonify(tuples)
  except TypeError as e:
    return flask.jsonify([])
  except MySQLdb.Error as e:
    return flask.jsonify([])
  finally:
    cur.close()

@app.route('/add_petition', methods=['POST'])
def add_petition():
  try:
    cur = mysql.connection.cursor()
    today = date.today()
    cur.execute("SELECT * from estadisticas WHERE dia = %s", [today])
    results = cur.fetchone()
    if results == None:
      cur.execute("INSERT INTO estadisticas(peticiones, dia) VALUES(1, %s)", [today])
    else:
      cur.execute("UPDATE estadisticas SET peticiones = %s WHERE dia = %s", [results[1] + 1, today])
    mysql.connection.commit()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
  except TypeError as e:
    return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
  except MySQLdb.Error as e:
    return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
  finally: 
    cur.close()

if __name__ == '__main__':
  app.run(host='0.0.0.0')