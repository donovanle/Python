from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt =  Bcrypt(app)

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def createuser(cls, data):
        hashed_pass = bcrypt.generate_password_hash(data["password"])
        user = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "email": data["email"],
            "password": hashed_pass
        }

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) " \
            "VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s, NOW(), NOW());"
        return connectToMySQL('login_schema').query_db(query, user)
    
    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('login_schema').query_db(query)
        users = []
        for item in results:
            users.append(cls(item))
        return users

    @classmethod
    def user_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_schema').query_db(query,data)
        if results:
            return cls(results[0]) 
        return False

    @classmethod
    def user_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login_schema').query_db(query,data)
        if results:
            return cls(results[0]) 
        return False
    
    @classmethod
    def validate_login(cls, data):
        user_valid = User.user_email(data)
        if not user_valid:
            flash("Invalid Email/Password","login")
            return False
        if not bcrypt.check_password_hash(user_valid.password, data["password"]):
            flash("Invalid Email/Password""login")
            return False
        return True
    
    @staticmethod
    def email_is_valid(email):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('login_schema').query_db(query,email)
        if len(results) >= 1:
            flash("Email Already In Use","register")
            is_valid=False
        return is_valid

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First Name must be at least 2 characters.","register")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last Name must be at least 2 characters.","register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.","register")
            is_valid = False
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash("Password does not match","register")
        return is_valid
    
