#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    teacher = {
        'name': 'Aiden',
        'email': 'luojin@simplecloud.cn'
    }
    course = {
        'name': 'Python Basic',
        'teacher': teacher,
        'user_count': 5348,
        'price': 199.0,
        'lab': None,
        'is_private': False,
        'is_member_course': True,
        'tags': ['python', 'big data', 'Linux']
    }
    return render_template('index.html', course=course)


# def main():
#     app = Flask(__name__)
#     app.config['TEMPLATES_AUTO_RELOAD'] = True
#     print('inside main()')

# if __name__ == '__main__':
#     main()
