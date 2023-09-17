from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Home'

@app.route('/login')
def login():
    return 'Log In'

@app.route('/sign-in')
def signin():
    return 'Sign In'

if (__name__ == '__main__'):
    app.run(debug=True)