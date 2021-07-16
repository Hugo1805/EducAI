from flask import Blueprint, jsonify
from flask_restful import Api
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
from cerberus import errors

from werkzeug.exceptions import BadRequest, InternalServerError, Unauthorized

#cerberus
class CustomErrorHandler(errors.BasicErrorHandler):
	def __init__(self, tree=None, custom_messages=None):
		super(CustomErrorHandler, self).__init__(tree)
		self.custom_messages = custom_messages or {}
	def _format_message(self, field, error):
		tmp = self.custom_messages
		for x in error.schema_path:
			try:
				tmp = tmp[x]
			except KeyError:
				return super(CustomErrorHandler, self)._format_message(field, error)
		if isinstance(tmp, dict):
			return super(CustomErrorHandler, self)._format_message(field, error)
		else:
			return tmp

#rest
class ExtendedAPI(Api):
    def handle_error(self, err):
        if isinstance(err, HTTPException):
            return jsonify({
                    'message': getattr(
                        err, 'description', HTTP_STATUS_CODES.get(err.code, '')
                    )
                }), err.code
        if not getattr(err, 'message', None):
            return jsonify({
                'message': 'Server has encountered some error'
                }), 500
        return jsonify(**err.kwargs), err.http_status_code

class InternalServerError(InternalServerError):
    def handle_error(self, err):
        if isinstance(err, HTTPException):
            return jsonify({
                    'message': getattr(
                        err, 'description', HTTP_STATUS_CODES.get(err.code, '')
                    )
                }), err.code
        if not getattr(err, 'message', None):
            return jsonify({
                'message': 'Server has encountered some error'
                }), 500
        return jsonify(**err.kwargs), err.http_status_code
class SchemaValidationError(BadRequest):
    message='go'

class EmailAlreadyExistsError(BadRequest):
    pass

class UnauthorizedError(Unauthorized):
    pass

class EmailDoesnotExistsError(BadRequest):
    pass

class BadtokenError(BadRequest):
    pass
