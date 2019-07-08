# -*- coding: utf-8 -*-

import json
from flask import request
from flask_jwt_extended import create_access_token
from app.api import api
from app.models.user import User
from app.common.utils import resp_json, Code


# 登录
@api.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if User.objects(username=username, password=password).first():
        access_token = create_access_token(identity=username)
        return resp_json(code=Code.SUCCESS, data=dict(access_token=access_token))

    return resp_json(code=Code.UNAUTHORIZED)


# 注册
@api.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if User.objects(username=username).first():
        return resp_json(Code.DUPLICATE_DATA)

    user = User(username=username, password=password).save()
    result = json.loads(user.to_json())
    result.pop('password')
    
    return resp_json(code=Code.SUCCESS, data=result)
