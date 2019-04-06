# coding: utf-8
from .db import db
import datetime

class User(db.Document): 
    username = db.StringField(required=True) 
    email = db.StringField(required=False)  
    password = db.StringField(required=False) 
    permissions = db.ListField()

    meta = {'collection': 'users', 'strict': False}