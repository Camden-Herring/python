
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe...'

@app.route('/')
def index():
    return render_template('form_ds.html')

@app.route('/user', methods = ['POST'])
def form():
    session['username'] = request.form['name']
    session['user_location'] = request.form['location']
    session['user_fav_language'] = request.form['fav_language']
    session['user_comments'] = request.form['comments']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show_ds.html')

if __name__=='__main__': 
    app.run(debug=True)