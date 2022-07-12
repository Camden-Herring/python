from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def greet_name(name):
    return render_template("hello.html",name = name)

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return word*num

if __name__=="__main__":
    app.run(debug=True)