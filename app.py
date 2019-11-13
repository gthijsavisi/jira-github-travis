from flask import Flask
APP = Flask(__name__)
# hello world route


@APP.route('/')
def hello_world():
    return 'NEW PIPELINE TEST - TRAVIS'