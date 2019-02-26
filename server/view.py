from server import app
import pickle
import pymongo
from flask import render_template, redirect, url_for, abort, flash, request
import json


@app.route('/')
def home():
    return render_template("main.html", date="2019-02-23")


@app.route('/api/get/<date>')
def get_entry(date):
    with open("accounting.json", "r", encoding='utf-8') as fj:
        table = json.load(fj)
    entry = table.get(date, {})
    if entry == {}:
        entry['status'] = False
    else:
        entry['status'] = True
    return json.dumps(entry)


@app.route('/api/set/<date>')
def set_entry(date):
    if 'costs' in request.form:
        with open("accounting.json", "r", encoding='utf-8') as fj:
            table = json.load(fj)
        table[date] = request.form.get('costs')
        with open("accounting.json", "w", encoding='utf-8') as fj:
            json.dump(fj, table)
        return True
    else:
        return False


@app.route('/test')
def test():
    return render_template('tmp.html')
