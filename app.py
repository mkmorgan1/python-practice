from flask import Flask
from testFunc import add

app = Flask(__name__)
app.run(debug=True)

@app.route("/")
def index():
    return f"{add(1, 5)}"


@app.route("/sup")
def sup():
    return "Sup"
