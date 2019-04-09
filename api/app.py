from flask import Flask
from flask_restful import Api

from flasgger import Swagger
from .db import db  

from os import path

from swagger import swagger_config
from .blueprints.user import user_blueprint
from .utils.encoders import CustomJsonEncoder

from annotations.auth import login_required

def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), '%s_instance' % mode
    ) 

    app = Flask('api',
                instance_path=instance_path,
                instance_relative_config=True)
    api = Api(app)

    app.config.from_object('api.default_settings')
    app.config.from_pyfile('config.cfg')
    app.config['SWAGGER'] = {
        'title': 'AuthServer RESTful',
        'uiversion': 1
    }
    swagger = Swagger(app, template=swagger_config)

    app.register_blueprint(user_blueprint)
 
    db.init_app(app) 

    app.json_encoder = CustomJsonEncoder
 
    return app
