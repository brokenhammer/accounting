from flask import Flask
import os
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.jinja_env.variable_start_string = '{{{{'
app.jinja_env.variable_end_string = '}}}}'
app.config.from_object('config')
app.config['WORK_DIR'] = os.getcwd()
if os.path.exists('instance/config.py'):
    app.config.from_pyfile('config.py')

import server.view