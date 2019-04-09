from flask import Flask
from flasgger import Swagger
from .db import db  

from os import path

from swagger import swagger_config
from .apps.user import user_blueprint 
from .utils.encoders import CustomJsonEncoder

from flask_spyne import Spyne 
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable 
from werkzeug.wsgi import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication
from .apps.user_soap import create_soap_app

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

    # SOAP services are distinct wsgi applications, we should use dispatcher
    # middleware to bring all aps together
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/soap': WsgiApplication(create_soap_app(app))
    })

    return app
