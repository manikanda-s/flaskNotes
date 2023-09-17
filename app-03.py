from flask import Flask

app = Flask(__name__)

@app.route('/home/<name>')
def home(name):
    return f'Hello world {name}'

if (__name__ == '__main__'):
    app.run(debug=True)