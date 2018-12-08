from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'José Javier'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'It\'s a beautiful day'
        },
        {
            'author': {'username': 'José'},
            'body': 'It\'s a big day'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)