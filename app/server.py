from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/')
def server():
    print("HELLLO")
    print(environ.get("ALCHEMY_URL"))
    return 'Hello, world'
