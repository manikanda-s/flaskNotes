from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index-07.html')
    

@app.route('/home', methods=['POST'])
def home():
    name = request.form.get('name')
    return render_template('output-07.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)