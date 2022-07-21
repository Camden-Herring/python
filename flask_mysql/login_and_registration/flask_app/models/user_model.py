from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

db_schema = "login_and_registration_schema"

class User:
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        return connectToMySQL(db_schema).query_db(query, data)

class User:
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db_schema).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])