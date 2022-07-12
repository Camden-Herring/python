from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index_cb.html")

@app.route('/<int:num1>')
def num_rows(num1,):
    return render_template("index_cb.html", num1 = num1)


if __name__=='__main__': 
    app.run(debug=True)