from flask import Flask

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  return "Fine"

@app.route('/tweet/<int:id>', methods=['POST'])
def register(id):
  return "TBD"

if __name__ == '__main__':
  app.run(host='0.0.0.0')