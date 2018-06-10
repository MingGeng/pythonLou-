#!/usr/bin/env python3

from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/news'
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def  __repr__(self):
        return '<Category %r>' % self.name

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)

    def __init__(self, id, title, created_time, category_id, content):
        self.id = id
        self.title = title
        self.created_time = created_time
        self.category_id = category_id
        self.content = content

    def __repr__(self):
        return '<Flie %r>' % self.title
        

@app.route('/')
def index():
    file_dict = {}
    files = File.query.all()
    for file in files:
        file_dict[file.title] = file

    return render_template('index.html', file_dict=file_dict)

@app.route('/files/<file_id>')
def file(file_id):
    file_details = {}
    fileid_list = []
    for file in File.query.all():
        fileid_list.append(file.id)

    target_file = File.query.filter_by(id=file_id).first()
    if target_file:
        file_details['file_id'] = target_file.id
        file_details['created_time'] = target_file.created_time
        file_details['content'] = target_file.content
        file_details['title'] = target_file.title
    else:
            abort(404)

    return render_template('file.html', file_details=file_details)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404




