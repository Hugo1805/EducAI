from flask import Response, request
from flask_restful import Resource
from tornado import gen, web, httpclient
from cerberus import Validator

from resources.errors import SchemaValidationError, CustomErrorHandler

from services.maestro_service import insertMaestro, listMaestros

class InsertMaestro(Resource):
    schema = {
    'nombre': {
        'required':True,
        'type':'string'
    },
    'apellido': {
        'required':True,
        'type':'string'
    },
    'especialidad': {
        'required':True,
        'type':'string'
    },
    'email': {
        'required':True,
        'type':'string'
    },
    'codigo_maestro': {
        'required':True,
        'type':'string'
    }
    }
    messages = {
        "nombres":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "apellidos":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "especialidad":{"required":"Campo obligatorio", "type":"Debe ser un string"},
        "email":{"required":"Campo obligatorio", "type":"Debe ser un email"},
        "codigo_maestro":{"required":"Campo obligatorio", "type":"Debe ser un string"}
    }
    def post(self):
        body = request.get_json()
        print(body)
        insertmaestro = Validator(self.schema, error_handler=CustomErrorHandler(custom_messages=self.messages))
        if insertmaestro.validate(body or {}):
            return insertMaestro(body['nombre'], body['apellido'], body['especialidad'], body['email'], body['codigo_maestro'])
        raise SchemaValidationError(insertmaestro.errors)

class ListMaestros(Resource):
    schema = {
    'codigo_maestro': {
        'required':True,
        'type':'string'
    }
    }
    messages = {
        "codigo_maestro":{"required":"Campo obligatorio", "type":"Debe ser un string"}  
    }
    def post(self):
        body = request.get_json()
        print(body)
        listmaestro = Validator(self.schema, error_handler=CustomErrorHandler(custom_messages=self.messages))
        if listmaestro.validate(body or {}):
            return listMaestros(body['codigo_maestro'].lower())
        raise SchemaValidationError(listmaestro.errors)
