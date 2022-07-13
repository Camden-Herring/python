from itertools import count
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe...'


@app.route('/')
def counter_refresh():
    if 'visits' in session: 
        session['visits'] = session.get('visits') + 1
        return render_template('index.html')
    else: 
        session['visits'] = 1
    return str(session.get('visits'))

@app.route('/destroy_session')
def destroy_session():
    session['visits'] = session.clear()
    return redirect('/')

# @app.route('/')
# def visits():
#     if 'visits' in session:
#         session['visits'] = session.get('visits') + 1  # reading and updating session data
#     else:
#         session['visits'] = 1 # setting session data
#     return "Total visits: {}".format(session.get('visits'))

# @app.route('/delete-visits/')
# def delete_visits():
#     session.pop('visits', None) # delete visits
#     return 'Visits deleted'


if __name__=='__main__': 
    app.run(debug=True)