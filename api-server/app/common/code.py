# -*- coding: utf-8 -*-


class Code:
    SUCCESS = 200
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    NOT_ALLOWED = 405
    UNPROCESSABLE = 422
    DUPLICATE_DATA = 1001
    NO_DATA = 10002
    RESP_JSON_ERROR = 10003

    msg = {
        SUCCESS: 'Success',
        NOT_FOUND: 'Not found',
        FORBIDDEN: 'Forbidden',
        UNAUTHORIZED: 'Unauthorized',
        NOT_ALLOWED: 'Method not allowed',
        UNPROCESSABLE: "Unprocessable",
        DUPLICATE_DATA: 'Duplicate data',
        NO_DATA: 'No data',
        RESP_JSON_ERROR: "Response json format error"
    }
