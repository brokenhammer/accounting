from server import app
import pickle
import pymongo
from flask import render_template,redirect,url_for,abort,send_file,send_from_directory

@app.route('/')
def hello_world():
    return 'Hello World!'