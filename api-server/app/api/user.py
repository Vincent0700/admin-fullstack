# -*- coding: utf-8 -*-

import json
from flask import request
from flask_jwt_extended import jwt_required
from app.api import api
from app.models.user import User
from app.common.utils import Code, resp_json


# 获取用户
@api.route('/user', methods=['GET'])
@jwt_required
def get_user():
    data = request.json
    username = data.get('username')
    user = User.objects(username=username).first()
    assert 1 == 2

    if user:
        result = json.loads(user.to_json())
        result.pop('password')
        return resp_json(code=Code.SUCCESS, data=result)

    return resp_json(code=Code.NO_DATA)
