#!/usr/bin/env python3
from flask import Flask, render_template
from flask_httpauth import HTTPDigestAuth
import settings

DEBUG_MODE = True
HOST_NAME = settings.HOST_NAME
PORT = settings.PORT
USER = settings.USER
PASSWORD = settings.PASSWORD
SECRET_KEY = settings.SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
auth = HTTPDigestAuth()
users = {USER: PASSWORD}


@auth.get_password
def get_pw(username: str):
    if username in users:
        return users.get(username)
    return None


@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host=HOST_NAME, port=PORT)
