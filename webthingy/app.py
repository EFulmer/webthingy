from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/post/<slug>")
def post(slug: str):
    return slug


@app.route("/about/")
def about():
    return "hello"
