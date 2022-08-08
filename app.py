from urllib import request
from flask import Flask
from requests import get

app = Flask(__name__)

@app.route("/")
def root():
    return {"message": "root"}

app.run(port=5000)