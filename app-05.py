from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index-05.html')

if __name__ == '__main__':
    app.run(debug=True)