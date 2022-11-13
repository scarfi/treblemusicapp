import os
from flask import Flask, render_template

static_folder = os.path.abspath('../frontend/static')
template_folder = os.path.abspath('../frontend/templates')
print(static_folder, template_folder)
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

@app.route('/')
def index():
    os.path.abspath('../frontend/static')
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/collaborate')
def collaborate():
    return render_template('collaborate.html')

@app.route('/share')
def share():
    return render_template('share.html')

@app.route('/produce')
def produce():
    return render_template('produce.html')

@app.route('/myprofile')
def myprofile():
    return render_template('myprofie.html')

@app.route('/reset-password')
def reset_password():
    return render_template('reset_password.html')

if __name__ == '__main__':
    app.config.from_pyfile('config.py')

    app.run(
        host=app.config.get('HOST'),
        port=app.config.get('PORT'),
    )