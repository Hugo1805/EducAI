from flask import request, Response
from flask_restful import Resource
import json

from database.models import Maestro
from services.lower_json_service import data_lower
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError

#POST
def insertMaestro(nombre, apellido, especialidad, email, codigo_maestro):
    try:
        body = request.get_json()
        print('body json service:', body)
        body_lower = data_lower(body)
        print('body_lower json service:', body_lower)
        maestro = Maestro(**body_lower)
        print('maestro json service:', maestro)
        maestro.save()
        id = maestro.id
        return {'id': str(id)}, 200
    except FieldDoesNotExist:
        raise SchemaValidationError
    except NotUniqueError:
        raise EmailAlreadyExistsError
    except Exception as e:
        raise InternalServerError

# Get
def listMaestros(codigo_maestro):
    try:
        print('codigo_maestro: ', codigo_maestro)
        maestro = Maestro.objects().get(codigo_maestro=codigo_maestro).to_json()
        print('maestro DB: ',maestro)
        maestro_response = json.loads(maestro)
        print(maestro_response) 
        maestro_json_response = {
                'codigo_maestro': maestro_response['codigo_maestro'],
                'email': maestro_response['email'],
                'nombre': maestro_response['nombre'] +' '+ maestro_response['apellido'],
                'especialidad' : maestro_response['especialidad']
            },201
        return maestro_json_response
    except FieldDoesNotExist:
        raise SchemaValidationError
    except NotUniqueError:
        raise EmailAlreadyExistsError
    except Exception as e:
        raise InternalServerError