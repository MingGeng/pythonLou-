#!/usr/bin/env python3

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.update({
    'SECTET_KEY': 'a random string'
})

#app.config.from_pyfile('real_path_of/config.py')
#app.config.from_envvar(variable_name)
#app.config.from_object(obj)
#app.config.from_json(filename)
#app.config.from_mapping(*mapping, **kwargs)

@app.route('/')
def index():
    return 'Index'
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)
@app.route('/user/<username>')
def user_index(username):
#    return 'Hello {}!'.format(username)
    return render_template('user_index.html', username=username) 


if __name__ == '__main__':
    app.run()
    print(app.config['SECRET_KEY'])




