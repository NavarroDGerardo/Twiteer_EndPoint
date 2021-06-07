from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/tweets', methods=['GET'])
def users_tweets():
  users = request.get('http://user:5000/users').json()

  tweets = []
  for user in users:
    tweets.append({
      user: user,
      tweets: get_tweets(user)
    })

  return jsonify(tweets)

def get_tweets(username):
  return request.get('http://api:5000/tweet/{}').format(username).json()

if __name__ == '__main__':
  app.run(host='0.0.0.0')