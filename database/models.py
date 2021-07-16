from .db import db
import os
from flask_bcrypt import generate_password_hash,check_password_hash


variable_mongo_educai_alias_user = os.getenv('MONGO_DB_ALIAS_USER')
variable_mongo_educai_alias_maestro = os.getenv('MONGO_DB_ALIAS_MAESTRO')
variable_mongo_educai_alias_curso = os.getenv('MONGO_DB_ALIAS_CURSO')
variable_mongo_educai_alias_nota = os.getenv('MONGO_DB_ALIAS_NOTA')

variable_monogo_educai_collecion_user = os.getenv('MONGO_DB_ALIAS_USER')
variable_monogo_educai_collecion_maestro = os.getenv('MONGO_DB_ALIAS_MAESTRO')
variable_monogo_educai_collecion_curso = os.getenv('MONGO_DB_ALIAS_CURSO')
variable_monogo_educai_collecion_nota = os.getenv('MONGO_DB_ALIAS_NOTA')

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8)
    nombres = db.StringField(required=True)
    apellidos = db.StringField(required=True) 
    tipo_documento = db.StringField(required=True)
    numero_documento = db.StringField(required=True)
    celular = db.StringField(required=True)
    carrera = db.StringField(required=True)
    ciclo = db.IntField(required=True)
    codigo_alumno = db.StringField(required=True)
    meta = {
        'db_alias': variable_mongo_educai_alias_user, 
        'collection': variable_monogo_educai_collecion_user
    }

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Maestro(db.Document):
    nombre = db.StringField(required=True)
    apellido = db.StringField(required=True)
    especialidad = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    codigo_maestro = db.StringField(required=True)
    meta = {
        'db_alias': variable_mongo_educai_alias_maestro, 
        'collection': variable_monogo_educai_collecion_maestro
    }
    
class Curso(db.Document):
    carrera = db.StringField(required=True)
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    dia_de_semana = db.StringField(required=True)
    hora_inicio = db.StringField(required=True)
    hora_final = db.StringField(required=True)
    ciclo = db.StringField(required=True)
    year = db.StringField(required=True) 
    codigo_curso = db.StringField(required=True)
    codigo_alumno = db.ReferenceField(User)
    codigo_maestro = db.ReferenceField(Maestro)
    meta = {
        'db_alias': variable_mongo_educai_alias_curso, 
        'collection': variable_monogo_educai_collecion_curso
    }
class Nota(db.Document):
    Notas = db.DictField()
    codigo_curso = db.ReferenceField(Curso)
    codigo_alumno = db.ReferenceField(User)
    codigo_maestro = db.ReferenceField(Maestro)
    meta = {
        'db_alias': variable_mongo_educai_alias_nota, 
        'collection': variable_monogo_educai_collecion_nota
    }

