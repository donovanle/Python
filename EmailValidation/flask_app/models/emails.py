from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def newemail(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) " \
            "VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('email_schema').query_db(query, data)
    @classmethod
    def displayemails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_schema').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails
    @classmethod
    def deleteemail(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL('email_schema').query_db(query, data)
    
    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL('email_schema').query_db(query,email)
        if len(results) >= 1:
            flash("Email taken")
            is_valid=False
        return is_valid