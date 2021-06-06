from flask import Flask, render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tweeter_app'

mysql = MySQL(app)

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
  return tuples

if __name__ == '__main__':
  app.run(host='0.0.0.0')