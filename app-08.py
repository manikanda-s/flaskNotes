from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

count = 1
names = []

@app.route('/')
def home():
    return render_template('index-08.html')

@app.route('/add', methods=['POST'])
def add():
    global count
    name = request.form.get('name')
    names.append([count, name])
    count += 1
    # print(names)
    return redirect(url_for('home'))

@app.route('/list')
def listOfNames():
    return render_template('list-08.html', names=names)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if (request.method == 'POST'):
        name = request.form.get('name')
        id = request.form.get('id')
        for person in names:
            if (person[0] == int(id)):
                person[1] = name
        return render_template('list-08.html', names=names)

    name = request.args.get('name')
    id = request.args.get('id')
    return render_template('edit-08.html', name=name, id=id)

@app.route('/delete/<id>')
def delete(id):
    for person in names:
        if (person[0] == int(id)):
            print(person)
            names.remove(person)
    return render_template('list-08.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)