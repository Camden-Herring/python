# make sure everything in backend works first

# go through each of the letters of CRUD

# build front end, then tie to the database

# create all the folders, install depencies, write a basic server.py and make sure everything boots up, introduce routes, introduce controllers/models

from flask_app import app
from flask_app.controllers import user_controller
from flask_app.models import user_model

if __name__=='__main__': 
    app.run(debug=True)

    