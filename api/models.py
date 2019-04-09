# coding: utf-8
from .db import db
import datetime
from passlib.apps import custom_app_context as pwd_context

class User(db.Document): 
    username = db.StringField(required=True) 
    email = db.StringField(required=False)    
    password = db.StringField()
    permissions = db.ListField(db.StringField())

    def hash_password(self, password):
        """
        Takes a plain password and stores a hash of it with the user.
        """
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        """
        Takes a plain password as argument and returns True if 
        the password is correct or False if not
        """ 
        return pwd_context.verify(password, self.password)

    meta = {'collection': 'users', 'strict': False}