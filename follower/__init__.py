from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException


def make_json_error(ex):
    response = jsonify(message=str(ex))
    if isinstance(ex, HTTPException):
        response.status_code = ex.code
    else:
        response.status_code = 500
    return response

app = Flask(__name__)
app.config.from_object('config')

for code in default_exceptions.iterkeys():
    app.error_handler_spec[None][code] = make_json_error
