# -*- coding: utf-8 -*-

import json
from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from app.common.utils import Code, resp_json

db = MongoEngine()


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('app.config')

    # Register api
    from app.api import api
    app.register_blueprint(api, url_prefix='/api')

    @app.after_request
    def after_request(response):
        status_code = int(response.status[:3])

        # Handle errors
        if status_code == 401:
            return resp_json(Code.UNAUTHORIZED)
        elif status_code == 403:
            return resp_json(Code.FORBIDDEN)
        elif status_code == 404:
            return resp_json(Code.NOT_FOUND)
        elif status_code == 405:
            return resp_json(Code.NOT_ALLOWED)
        elif status_code == 422:
            return resp_json(Code.UNPROCESSABLE)

        # Filter response data
        json_data = response.json
        if 'data' in json_data:
            data = json_data['data']
            if data and '_id' in data:
                data['_id'] = data['_id']['$oid']
                response.set_data(json.dumps(json_data))

        # Enable CORS
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers

        return response

    # Init MongoDB
    db.init_app(app)

    # Init JWT
    JWTManager(app)
    return app
