from flask import Response,request
from flask_restful import Resource


class Hello(Resource):

    def get(self):
        hello_v = "<p>Hello, World!</p>"
        return Response(hello_v,status=200)