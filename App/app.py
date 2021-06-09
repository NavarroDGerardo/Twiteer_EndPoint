import socket
import csv
import logging
from pathlib import Path
from datetime import date
import requests
from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/', methods=['GET'])
def landing_page():
  tweets = requests.get('http://aggregate:5000/tweets').json()
  add_petition()
  create_log(tweets)
  return render_template("index.html", tweets=tweets)

@app.route("/addUser")
def addUser():
    return render_template("addUsers.html")

@app.route("/agregar_user", methods=['POST'])
def agregar_user():
  name = request.form["name"]
  requests.post('http://user:5000/add/{}'.format(name))
  add_petition()
  return redirect("/")

def get_user_ip():
  hostname = socket.gethostname()
  ip_address = socket.gethostbyname(hostname)
  return ip_address

def create_log(tweets):
  ip = get_user_ip()
  Path("./log_responses").mkdir(exist_ok=True)
  with open("log_responses/{}-{}.csv".format(ip, date.today()), 'w', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["username", "Content"])
    for tweet in tweets:
      t = tweet["tweets"][0] if len(tweet["tweets"]) > 0 else ""
      writer.writerow([tweet["user"], t])

def add_petition():
  return requests.post('http://user:5000/add_petition')


if __name__ == '__main__':
  app.logger.setLevel(logging.INFO)
  app.run(host='0.0.0.0')