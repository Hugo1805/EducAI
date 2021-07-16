from flask import Response, request
from flask_restful import Resource
from tornado import gen, web, httpclient
from cerberus import Validator

from resources.errors import SchemaValidationError, CustomErrorHandler

from services.user_service import insertUsers, listUsers

class InsertUser(Resource):
    schema = {
    'email': {
        'required':True,
        'type':'string'
    },
    'password': {
        'required':True,
        'type':'string'
    },
    'nombres': {
        'required':True,
        'type':'string'
    },
    'apellidos': {
        'required':True,
        'type':'string'
    },
    'tipo_documento': {
        'required':True,
        'type':'string'
    },
    'numero_documento': {
        'required':True,
        'type':'string'
    },
    'celular': {
        'required':True,
        'type':'string'
    },
    'carrera': {
        'required':True,
        'type':'string'
    },
    'ciclo': {
        'required':True,
        'type':'string'
    },
    'codigo_alumno': {
        'required':True,
        'type':'string'
    }
    }
    messages = {
        "email":{"required":"Campo obligatorio", "type":"Debe ser un email"},
        "password":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "nombres":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "apellidos":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "tipo_documento":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "numero_documento":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "celular":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "carrera":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "ciclo":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "codigo_alumno":{"required":"Campo obligatorio", "type":"Debe ser un string"},  
    }
    def post(self):
        body = request.get_json()
        print(body)
        insertuser = Validator(self.schema, error_handler=CustomErrorHandler(custom_messages=self.messages))
        print(insertuser)
        if insertuser.validate(body or {}):
            return insertUsers(body['email'], body['password'], body['nombres'], body['apellidos'], body['tipo_documento'], body['numero_documento'], body['celular'], body['carrera'], body['ciclo'], body['codigo_alumno'])
        raise SchemaValidationError(insertuser.errors)

class ListUser(Resource):
    schema = {
    'codigo_alumno': {
        'required':True,
        'type':'string'
    }
    }
    messages = {
        "codigo_alumno":{"required":"Campo obligatorio", "type":"Debe ser un string"}  
    }
    def post(self):
        body = request.get_json()
        print(body)
        listuser = Validator(self.schema, error_handler=CustomErrorHandler(custom_messages=self.messages))
        print(listuser)
        if listuser.validate(body or {}):
            return listUsers(body['codigo_alumno'].lower())
        raise SchemaValidationError(listuser.errors)
