from flask_app.config.mysqlconnection import connectToMySQL
db_schema = 'login_and_registration_schema'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.user_email = data['user_email']
        self.password = data['password']

    @classmethod
    def create_user(cls, data):
        query = "insert into users (first_name, last_name, user_email, password), \
        values( %(f_name)s, %(l_name)s, %(u_email)s, %(u_password)s);"

        return connectToMySQL(db_schema).query_db(query, data)