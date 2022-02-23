from flask import Flask, url_for, escape
app=Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, Dodoro!</h1><img src='http://helloflask.com/totoro.gif'>"

@app.route('/user/<name>')
def user_page(name):
    return f"User Page<br>" \
           f"User:{escape(name)}"

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name="王八蛋"))
    print(url_for('user_page', name="Jacky!"))
    print(url_for('test_url_for'))
    return "test page"


