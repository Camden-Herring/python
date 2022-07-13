from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index_bc.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

@app.route("/show")
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

if __name__=='__main__': 
    app.run(debug=True)