from .hello import Hello
from .user import InsertUser, ListUser
from .maestro import InsertMaestro, ListMaestros

def initialize_routes(api):

    #USER

    api.add_resource(InsertUser, '/api/v1/insertuser')
    api.add_resource(ListUser, '/api/v1/listuser')

    #MAESTRO

    api.add_resource(InsertMaestro, '/api/v1/insertmaestro')
    api.add_resource(ListMaestros, '/api/v1/listarmaestro')

    #HELLO
    api.add_resource(Hello, '/api/v1/hello')


