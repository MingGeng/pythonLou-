#!/usr/bin/env python3

from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/')
def index():
    file_dict = {}
    path = '/home/shiyanlou/shiyanlou_python_louPlus/challenge6/files'
    file_list = os.listdir(path)
    for filename in file_list:
        with open(os.path.join(path, filename)) as file:
            file_dict[filename] = json.loads(file.read())

    return render_template('index.html', file_dict=file_dict)

@app.route('/files/<filename>')
def file(filename):
    file_details = {}
    filename = filename + '.json'
    path = '/home/shiyanlou/shiyanlou_python_louPlus/challenge6/files'
    file_list = os.listdir(path)
    if filename not in file_list:
        abort(404)
    else:
        with open(os.path.join(path, filename)) as file:
            file_details = json.loads(file.read())

    return render_template('file.html', file_details=file_details)
    


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
