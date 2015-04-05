from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
import pylibmc


def make_json_error(ex):
    response = jsonify(message=str(ex))
    if isinstance(ex, HTTPException):
        response.status_code = ex.code
    else:
        response.status_code = 500
    return response

app = Flask(__name__)
app.config.from_object('config')
mc = pylibmc.Client(app.config.get('MEMCACHED_HOST', '127.0.0.1'),
                    binary=True,
                    behaviors={'tcp_nodelay': True, 'ketama': True})

for code in default_exceptions.iterkeys():
    app.error_handler_spec[None][code] = make_json_error
