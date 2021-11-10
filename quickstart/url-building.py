from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hallo Metaverse" + __name__

@app.route('/home/<nama>')
def home(nama):
    return "ini adalah home"+nama

@app.route('/next')
def next():
    return"ini adalah next"