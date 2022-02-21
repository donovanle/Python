from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User():
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def createuser(cls, data):
        query = "INSERT INTO user (name, location, language, comment) " \
            "VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        return connectToMySQL('dojo_survery_schema').query_db(query, data)
    @classmethod
    def showuser(cls):
        query = "SELECT * FROM user ORDER BY user.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survery_schema').query_db(query)
        return User(results[0]) 
    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(survey['comment']) < 3:
            is_valid = False
            flash("Comment must be at least 3 characters.")
        return is_valid