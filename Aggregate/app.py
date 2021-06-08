from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/tweets', methods=['GET'])
def users_tweets():
  users = requests.get('http://192.168.1.73:5001/users').json()
  usertweets = []
  for user in users:
    username = user[0]
    usertweets.append({
      "user": username,
      "tweets": get_tweets(username)
    })
  return jsonify(usertweets)

def get_tweets(username):
  return requests.get('http://192.168.1.73:5002/tweet/{}'.format(username)).json()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5003)