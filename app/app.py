from flask import Flask
from redis import Redis

app = Flask(__name__)

redis = Redis(host="redis")

@app.route("/")
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
