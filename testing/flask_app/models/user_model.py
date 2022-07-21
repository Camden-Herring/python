from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import EMAIL_REGEX, db_schema
from flask import flash

db_schema = "login_and_registration_schema"

class User:

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['user_email']
        self.password = data['password']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, user_email, password) VALUES (%(first_name)s, %(last_name)s, %(user_email)s, %(password)s);"
        return connectToMySQL(db_schema).query_db(query, data)


    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE user_email = %(user_email)s;"
        result = connectToMySQL(db_schema).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_registration(data):
        # breakpoint()
        print(data)
        query = "select * from users where user_email = %(email)s"
        results = connectToMySQL(db_schema).query_db(query, data)
        is_valid = True
        # breakpoint()
        # ^^ is validating that the email is not already registered
        if len(results) >= 1:
            flash("email already taken", "error_registration_email")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("name needs at least 2 characters", "error_registration_first_name")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("name needs at least 2 characters", "error_registration_last_name")
            is_valid = False
        if len(data['password']) < 8:
            flash("password needs at least 8 characters", "error_registration_password_length")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("invalid email", "error_registration_email")
            is_valid = False
        if data['password'] != data['password_confirmation']:
            flash("invalid password, does not match", 'error_registration_password')
            is_valid = False
            
        return is_valid