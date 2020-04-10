#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
