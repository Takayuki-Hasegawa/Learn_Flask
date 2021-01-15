from flask import Flask, render_template, request
from flask.globals import request

app = Flask(__name__)


@app.route("/")
def TopPage():
    param = "Hello, Here is Top Page"
    return render_template("head.html", param=param)


@app.route("/", methods=["post"])
def post():
    param = request.form["param"]
    return render_template("head.html", param=param)


if __name__ == "__main__":
    app.run(debug=True)
