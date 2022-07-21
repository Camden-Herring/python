from flask_app import app
from flask_app.models.user_model import User
from flask import request, redirect, session, flash, render_template
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def login_registration():

    return render_template('login_register.html')

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    if User.validate_registration(request.form) == False:
        return redirect('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "user_email": request.form['email'],
        "password" : pw_hash
    }
    print(data)
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/logged_in")


@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "user_email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", 'error_login_credentials')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", 'error_login_credentials')
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/logged_in")

@app.route('/logged_in')
def display_info():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('/logged_in.html')

@app.route('/user/logout')
def process_logout():
    session.clear()
    return redirect('/')
