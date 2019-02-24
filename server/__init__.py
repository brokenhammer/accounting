from flask import Flask
import os

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config['WORK_DIR'] = os.getcwd()
if os.path.exists('instance/config.py'):
    app.config.from_pyfile('config.py')

import server.view