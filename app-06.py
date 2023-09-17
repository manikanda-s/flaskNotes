from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    name = "manikandan"
    return render_template('index-06.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)