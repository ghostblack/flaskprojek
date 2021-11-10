from flask import Flask
from werkzeug.utils import escape
app = Flask(__name__)

@app.route('/projek/')
def show_user():
    return "The Projek"
@app.route('/home')
def home():
    return "ini adalah home"

@app.route('/next')
def next():
    return"ini adalah next"