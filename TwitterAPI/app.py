from twitter_api import TwitterAPI
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/tweet/<string:user>', methods=['POST'])
def register(user):
  api = TwitterAPI()
  return flask.jsonify(api.get_user_timeline(user))

if __name__ == '__main__':
  app.run(host='0.0.0.0')