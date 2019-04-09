# coding: utf-8
import os
import logging 
from flask import (
    request, jsonify, session
) 
from ..models import User  
from flask_httpauth import HTTPBasicAuth
from functools import wraps
 
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
    return jsonify({'error': "bad authorization info"}), 401

def make_login():
    auth = request.authorization 
    valid = check_auth(auth.username, auth.password)
    if not auth or not valid:
        return False
    session['username'] = auth.username
    return True

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs): 
        auth = request.authorization 
        valid = check_auth(auth.username, auth.password)
        if not auth or not valid or not session.get('username'):
            return authenticate()
        session['username'] = auth.username
        return f(*args, **kwargs)
    return decorated

def roles_accepted(permission): 
    def decorator(f):             
        @wraps(f)                               
        def decorated(*args,**kwargs):   
            auth = request.authorization 
            if not check_permission(permission, auth.username):
                return jsonify({'error': "you don't have authorization"}), 401                          
            return f(*args,**kwargs)            
        return decorated                                          
    return decorator  