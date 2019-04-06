# coding: utf-8
import os
import logging
from bson import ObjectId 
from flask import (
    Blueprint, request, current_app, send_from_directory, jsonify
) 
from ..models import User 
rom flasgger import swag_from 

logger = logging.getLogger(__name__)
user_blueprint = Blueprint('user', __name__, url_prefix="/api")

@user_blueprint.route("/users", methods=["GET"]) 
def get_users():
    users = User.objects.all()
    return jsonify({'users': users}), 400


@user_blueprint.route("/user", methods=["GET"])  
def get_user():
    user_id = request.headers.get('user_id')
    if user_id:
        if not ObjectId.is_valid(user_id):
            return jsonify({'error': 'Invalid user id.'}), 400
        
        user = User.objects.get(_id=ObjectId(user_id))  

    return jsonify({'user_id': user}), 400

@user_blueprint.route("/user/<username>", methods=["DELETE"])  
def delete_user(username): 
    if username: 
        user = User.objects.get(username=username).delete()

    return jsonify({'status': "ok"}), 400

@user_blueprint.route("/user", methods=["POST"])   
def create_user():
    content = request.json
    username = content.get('username')
    email = content.get('email')
    password = content.get('password')
    permissions = content.get('password')
    print(permissions)
    
    user = User(username=username, email=email, password=password)
    user.save()

    return jsonify({'status': "ok"}), 400