from flask import Flask
from testFunc import add

app = Flask(__name__)


@app.route("/")
def index():
    return f"{add(1, 2)}"


@app.route("/sup")
def sup():
    return "Sup"
