from flask import Flask

app = Flask(__name__)

@app.route('/')
def server():
    print("HELLLO")
    return 'Hello, world'
