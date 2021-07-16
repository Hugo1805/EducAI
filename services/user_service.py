from flask import request, Response
from flask_restful import Resource
import json

from database.models import User
from services.lower_json_service import data_lower
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError

#POST
def insertUsers(email,password,nombres,apellidos,tipo_documento,numero_documento,celular,carrera,ciclo,codigo_alumno):
    try:
        body = request.get_json()
        print('body json service:', body)
        body_lower = data_lower(body)
        print('body_lower json service:', body_lower)
        user = User(**body_lower)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200
    except FieldDoesNotExist:
        raise SchemaValidationError
    except NotUniqueError:
        raise EmailAlreadyExistsError
    except Exception as e:
        raise InternalServerError

# Get
def listUsers(codigo_alumno):
    try:
        user = User.objects().get(codigo_alumno=codigo_alumno).to_json()
        print('user DB: ',user)
        user_response = json.loads(user)
        print(user_response) 
        user_json_response = {
                'codigo_alumno': user_response['codigo_alumno'],
                'email': user_response['email'],
                'nombre': user_response['nombres'] +' '+ user_response['apellidos'],
                'ciclo' : user_response['ciclo'],
                'carrera': user_response['carrera']
            },201
        print(user_json_response)
        return user_json_response
        return Response(user_json_response, mimetype="application/json")
    except FieldDoesNotExist:
        raise SchemaValidationError
    except NotUniqueError:
        raise EmailAlreadyExistsError
    except Exception as e:
        raise InternalServerError