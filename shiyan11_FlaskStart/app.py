#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
app.config.update({
    'SECTET_KEY': 'a random string'
})
@app.route('/')
def index():
    return 'Hello Flask!'

if __name__ == '__main__':
    app.run()
