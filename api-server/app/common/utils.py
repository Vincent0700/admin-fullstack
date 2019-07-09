# -*- coding: utf-8 -*-

import json
from flask import Response
from app.common.code import Code


def resp_json(code: Code, data=None) -> Response:
    if data is None:
        data = {}

    if isinstance(data, str):
        try:
            data = json.loads(data)
        except TypeError:
            code = Code.RESP_JSON_ERROR

    ret_code = 200
    if code < 1000:
        ret_code = code

    data = json.dumps({
        'code': code,
        'msg': Code.msg[code],
        'data': data,
    })
    return Response(data, status=ret_code, mimetype='application/json')
