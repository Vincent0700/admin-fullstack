# -*- coding: utf-8 -*-

from app import db


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)

    meta = {
        'collection': 'user',
        'ordering': ['-create_at'],
        'strict': False,
    }
