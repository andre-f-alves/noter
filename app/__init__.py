from flask import Flask

app = Flask(__name__)

app.debug = True

@app.route('/')
def homepage():
  return '<h1>Hey! Welcome to my site!</h1>'
