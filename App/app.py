from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/', methods=['GET'])
def landing_page():
  return render_template("index.html")

@app.route('/tweets', methods=['GET'])
def all_tweets():
  return "TBD"

if __name__ == '__main__':
  app.run(host='0.0.0.0')