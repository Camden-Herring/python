from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all_users()
    # print(users)
    return render_template('read.html', users = users)

@app.route('/create_user', methods = ['GET','POST'])
def create_new_user():

    if request.method == "GET":
        return render_template('create.html')


    else:

        data = {
            "f_name" : request.form['f_name'],
            "l_name" : request.form['l_name'],
            "u_email" : request.form['u_email']
        }

        User.create_user(data)

        return redirect('/')

@app.route('/user/<int:id>')
def show_one_user(id):
    data = {
        "id" : id
    }

    return render_template('one_user.html', user = User.get_one_user(data))

@app.route('/update/user/<int:id>')
def edit_user(id):
    data  = {
        "id" : id
    }
    
    return render_template('edit.html', user = User.get_one_user(data))

@app.route('/update/user', methods = ["POST"])
def update():
    User.update_user(request.form)
    return redirect ('/')

@app.route('/delete/user/<int:id>')
def delete_user(id):
    data = {
        "id" : id
    }
    User.delete_user(data)
    return redirect('/')