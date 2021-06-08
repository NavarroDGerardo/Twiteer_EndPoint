import socket
import requests
from flask import Flask, render_template, request
from werkzeug.utils import redirect
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/', methods=['GET'])
def landing_page():
  tweets = requests.get('http://192.168.1.73:5003/tweets').json()
  return render_template("index.html", tweets=tweets)

@app.route("/addUser")
def addUser():
    return render_template("addUsers.html")

@app.route("/agregar_user", methods=['POST'])
def agregar_user():
  name = request.form["name"]
  response = requests.post('http://192.168.1.73:5001/add/{}'.format(name))
  return redirect("/")

def get_user_ip():
  hostname = socket.gethostname()
  ip_address = socket.gethostbyname(hostname)
  return ip_address


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)