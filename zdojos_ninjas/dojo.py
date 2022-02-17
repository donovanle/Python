from mysqlconnection import connectToMySQL

class Dojo():
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def createdojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) " \
            "VALUES (%(name)s, NOW(), NOW())"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

class Ninja():
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id= data ['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_one_dojo(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        results= connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        ninjas_dojo = []
        for ninja in results:
            ninjas_dojo.append( cls(ninja) )
        return ninjas_dojo
    @classmethod
    def createninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) " \
            "VALUES (%(name)s, NOW(), NOW())"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)