from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_app.models.user_model import User

@app.route('/', methods = ['GET','POST'])
def login_page():
    
    data = {
        "f_name" : request.form['f_name'],
        "l_name" : request.form['l_name'],
        "u_email" : request.form['u_email'],
        "u_password" : request.form['u_password']
    }

    return render_template('root.html')