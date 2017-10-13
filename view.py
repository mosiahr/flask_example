from app import app
from flask import render_template


@app.route('/')
def index():
    hello='Hello'
    return render_template('index.html', hello=hello)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


