from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS

from database.db import  initialize_db

from resources.errors import errors

#APP
app = Flask(__name__)

app.config.from_envvar('ENV_FILE_LOCATION')

# imports requiring app and mail
from resources.routes import initialize_routes

#CORS
cors = CORS(app)

# API
api = Api(app,errors=errors)

#Bcrypt
bcrypt = Bcrypt(app)

#JWT
jwt = JWTManager(app)


#Database
initialize_db(app)

#Restfull routes

initialize_routes(api)

if __name__ == "__main__":
    app.run()
