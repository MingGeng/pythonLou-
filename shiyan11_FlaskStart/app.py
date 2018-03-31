#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for, request, make_response, abort
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
#    return 'Index'
#    return redirect(url_for('user_index', username='default'))    
    username = request.cookies.get('username')
    if username == 'invalid':
        abort(404)
    else:
        return '<h1>Hello {} !</h1>'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/user/<username>')
def user_index(username):
#    return 'Hello {}!'.format(username)
    print(request.headers.get('User-Agent'))
#    page = request.args.get('page')
#    per_page = request.args.get('per_page')
#    form1 = request.form.get('form1')
#    method = request.method.get('')
    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username', username)
#    return render_template('user_index.html', username=username) 
    if username == 'invalid':
        abort(404)
    return resp

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404







if __name__ == '__main__':
    app.run()
    print(app.config['SECRET_KEY'])




