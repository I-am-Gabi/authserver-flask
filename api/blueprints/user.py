# coding: utf-8
import os
import logging
from bson import ObjectId 
from flask import (
    Blueprint, request, current_app, send_from_directory, jsonify, session
) 
from ..models import User 
from ..annotations.auth import login_required, roles_accepted, make_login
from flasgger import swag_from 
from flask_restful import Resource, abort, reqparse

logger = logging.getLogger(__name__)
user_blueprint = Blueprint('user', __name__, url_prefix="/api")

# 200 OK request has been processed successfully [PUT, POST, DELETE]
# 201 CREATED one or more new resources have been successfully created 
# 204 NO CONTENT no content to send in the response [PUT, POST,  DELETE]
# 

parser = reqparse.RequestParser()

class User(Resource):
    def get(self, username):
        if not User.objects(username=username):
            return jsonify({'error': "user doesn't exist"}), 400

        user = User.objects.get(username=username)  
        return jsonify({'username': user}), 400

    def delete(self, username):
        if not User.objects(username=username):
            return jsonify({'error': "user doesn't exist"}), 400

        user = User.objects.get(username=username).delete()
        return jsonify({}), 204
    
    def put(self, username):
        args = parser.parse_args()
        user = User.objects.get(username=username)
        user.update(
            set__username=args.get('username'),
            set__password=args.get('password'),
            set__permissions=args.get('permissions'), 
        )

        return jsonify({}), 204
