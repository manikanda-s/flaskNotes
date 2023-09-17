from flask import Flask, request

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Name : {name} and age : {age}'

if __name__ == '__main__':
    app.run(debug=True)