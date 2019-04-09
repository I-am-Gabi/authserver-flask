# coding: utf-8
import os
import logging 
from flask import (
    request, jsonify, session
) 
from ..models import User  
from flask_httpauth import HTTPBasicAuth
from functools import wraps

from ..utils.token import validate_token, save_token
import tokenlib
 
def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """ 
    if not User.objects(username=username):
        return False
    user = User.objects.get(username=username) 
    if not user or not user.verify_password(password):
        return False
    return True

def check_permission(permission, username):
    user = User.objects.get(username=username) 
    if permission in user.permissions:   
        return True
    return False

def authenticate(msg="login required"):
    """Sends a 401 response that enables basic auth"""
    return jsonify({'error': msg}), 401

def make_login(username, password):  
    valid = check_auth(username, password)
    if not valid:
        return None
    session['username'] = username
    token = tokenlib.make_token({"username": username}, secret="AUTH_SERVER") 
    return token

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs): 
        token = request.headers.get('Authorization')
        result = validate_token(str(token))
        if not result:
            return authenticate(result)
        return f(*args, **kwargs)
    return decorated

def roles_accepted(permission): 
    def decorator(f):             
        @wraps(f)                               
        def decorated(*args,**kwargs):   
            username = session.get('username')
            data_token = request.headers.get('Authorization')
            valid = validate_token(str(data_token))
            if not check_permission(permission, username) and not valid:
                return jsonify({'error': "you don't have authorization"}), 401                          
            return f(*args,**kwargs)            
        return decorated                                          
    return decorator  