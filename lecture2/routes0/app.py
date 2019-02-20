from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/doggo")
def doggo():
    return "Hello, Doggo!"

@app.route("/despacito")
def despacito():
    return "DES. PA. CITO"