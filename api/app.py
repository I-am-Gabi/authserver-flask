from flask import Flask
from flasgger import Swagger
from .db import db  

from os import path

from swagger import swagger_config
from .blueprints.user import user_blueprint
from .utils.encoders import CustomJsonEncoder

def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), '%s_instance' % mode
    ) 

    app = Flask('api',
                instance_path=instance_path,
                instance_relative_config=True)

    app.config.from_object('api.default_settings')
    app.config.from_pyfile('config.cfg')

    app.register_blueprint(user_blueprint)

    app.logger.propagate = True

    db.init_app(app)

    app.logger.propagate = True

    app.json_encoder = CustomJsonEncoder
 
    swagger = Swagger(app, template=swagger_config)

    return app
