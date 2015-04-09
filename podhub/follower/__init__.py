import util
from flask import Flask
from os.path import expanduser
from pkgutil import extend_path
from werkzeug.exceptions import default_exceptions
import os
import pylibmc

__path__ = extend_path(__path__, __name__)


app = Flask(__name__)
app.config.update(
    MEMCACHED_HOST='127.0.0.1',
    URL_PARSE_TIMEOUT=86400,  # 1 day
)

# Override app.config from externalized config files. First checks in user's
# homedir then at the system level in /etc/.
if os.access(expanduser('~/.config/podhub/follower/config.py'), os.R_OK):
    app.config.from_pyffile('~/.config/podhub/follower/config.py', silent=True)
elif os.access('/etc/podhub/follower/config.py', os.R_OK):
    app.config.from_pyffile('/etc/podhub/follower/config.py', silent=True)

if not app.debug:
    from logging import FileHandler
    import logging

    file_handler = FileHandler(
        app.config.get('LOG_FILE', '/var/log/podhub/follower/app.log'))
    file_handler.setLevel(
        getattr(logging, app.config.get('LOG_LEVEL', 'WARNING')))
    app.logger.addHandler(file_handler)

mc = pylibmc.Client([app.config.get('MEMCACHED_HOST', '127.0.0.1')],
                    binary=True,
                    behaviors={'tcp_nodelay': True, 'ketama': True})

for code in default_exceptions.iterkeys():
    app.error_handler_spec[None][code] = util.make_json_error

from . import views
