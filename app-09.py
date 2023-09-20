from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        'id': 1,
        'name': 'mani',
        'age': 20
    },
    {
        'id': 2,
        'name': 'kumar',
        'age': 22
    },
    {
        'id': 3,
        'name': 'ganesh',
        'age': 19
    }
    ,{
        'id': 4,
        'name': 'arun',
        'age': 20
    }
]

@app.route('/')
def get_all():
    return jsonify(students)

@app.route('/<int:id>')
def get_one(id):
    student = students[id]
    return jsonify(student)



if __name__ == '__main__':
    app.run(debug=True)