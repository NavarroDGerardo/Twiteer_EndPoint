import socket
from flask import Flask, render_template, request
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

@app.route('/', methods=['GET'])
def landing_page():
  return render_template("index.html")

@app.route('/tweets', methods=['GET'])
def all_tweets():
  tweets = request.get('https://aggregate:5000/tweets').json()
  return render_template("index.html", tweets=tweets)

@app.route("/addUser")
def addUser():
    return render_template("addUsers.html")

@app.route("/agregar_user", methods=['POST'])
def agregar_user():
  name = request.form["name"]
  cur = mysql.connection.cursor()
  cur.execute( "INSERT INTO users (name) VALUES (%s)", [name])
  mysql.connection.commit()
  cur.close()
  return render_template("index.html")

def get_user_ip():
  hostname = socket.gethostname()
  ip_address = socket.gethostbyname(hostname)
  return ip_address


if __name__ == '__main__':
  app.run(host='0.0.0.0')