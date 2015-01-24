# -*- coding:utf-8 -*-
from flask import Flask,render_template

app = Flask(__name__)

from flask.ext.bootstrap3 import Bootstrap
import time,datetime
import blog.views
from blog.models import User
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html')

@app.route('/admin')
def admin():
    user = User.query.filter_by(username='peter').first()
    return render_template('user.html', user=user)

if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(debug=True,host='0.0.0.0')
