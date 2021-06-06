from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/tweets', methods=['GET'])
def users_tweets():
  users = request.get('http://user:5000/users').json()
  tweets = [get_tweets(users[i[0]]) for i in range(0, len(users))]
  return jsonify(tweets)

def get_tweets(id):
  return request.get('http://api:5000/{}').format(id).json()

if __name__ == '__main__':
  app.run(host='0.0.0.0')