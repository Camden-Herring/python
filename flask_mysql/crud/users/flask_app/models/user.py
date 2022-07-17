
from flask_app.config.mysqlconnection import connectToMySQL
db_schema = "users_schema"


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_email = data['user_email']

    @classmethod
    def get_all_users(cls):

        query = "select * from users;"
        results = connectToMySQL(db_schema).query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def create_user(cls, data):
        print(data)
        query = "insert into users (first_name, last_name, created_at, updated_at, user_email) \
        values (%(f_name)s, %(l_name)s, NOW(), NOW(), %(u_email)s);"

        return connectToMySQL(db_schema).query_db(query, data)

    @classmethod
    def get_one_user(cls, data):
        query = "select * from users where id = %(id)s;"
        result = connectToMySQL(db_schema).query_db(query, data)
        return cls(result[0])
        
    @classmethod
    def update_user(cls,data):
        query = 'update users \
                set first_name = %(f_name)s, last_name = %(l_name)s, updated_at = NOW(),  user_email = %(u_email)s \
                where id = %(id)s;'
        return connectToMySQL(db_schema).query_db(query, data)
        

    @classmethod
    def delete_user(cls, data):
        query = 'delete from users where id = %(id)s;'
        return connectToMySQL(db_schema).query_db(query, data)