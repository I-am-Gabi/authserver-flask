# coding: utf-8
import os
import logging 
from flask import (
    request, jsonify, session
) 
from ..models import User  
from flask_httpauth import HTTPBasicAuth
from functools import wraps

from ..utils.token import validate_token
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

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return jsonify({'WWW-Authenticate': 'Basic realm=Login Required'}), 401

def make_login(username, password):  
    valid = check_auth(username, password)
    if not valid:
        return None
    session['username'] = username
    session['token'] = tokenlib.make_token({"username": username}, secret="AUTH_SERVER")
    return session['token']

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session["username"]:
            return jsonify({'error': "user already logged"}), 200
        
        valid = check_auth(username, password)
        if not auth or not valid and not session['username']:
            return authenticate()
        session['username'] = username
        session['token'] = tokenlib.make_token({"username": username}, secret="AUTH_SERVER")
        return f(*args, **kwargs)
    return decorated

def roles_accepted(permission): 
    def decorator(f):             
        @wraps(f)                               
        def decorated(*args,**kwargs):   
            auth = request.authorization 
            if not check_permission(permission, username):
                return jsonify({'error': "you don't have authorization"}), 401                          
            return f(*args,**kwargs)            
        return decorated                                          
    return decorator  