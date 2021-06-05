from flask import Flask

app = Flask(__name__)

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
  return "TBD"

if __name__ == '__main__':
  app.run(host='0.0.0.0')