from server import app
import pickle
import pymongo
import datetime
from flask import render_template, redirect, url_for, abort, flash, request
import json


@app.route('/')
def home():
    now = datetime.datetime.now()
    date_str = datetime.datetime.strftime(now,format='%Y-%m-%d')
    return render_template("main.html", date=date_str)


@app.route('/api/get/<date>')
def get_entry(date):
    with open("accounting.json", "r", encoding='utf-8') as fj:
        table = json.load(fj)
    entry = table.get(date, {})
    if entry == {}:
        rtn = {'status':False}
    else:
        rtn = {'costs':entry, 'status':True}
    return json.dumps(rtn)


@app.route('/api/set',methods=['POST'])
def set_entry():
    data = json.loads(request.data)
    a = json.loads(request.data)
    date = data.get('date', None)
    costs = data.get('costs', None)
    if not (date and costs):
        return 'false'
    else:
        with open('accounting.json') as fj:
            json_record = json.load(fj)
        json_record[date] = costs
        with open('accounting.json', 'w') as fj:
            json.dump(json_record, fj)
        return 'true'

@app.route('/api/delete/<date>',methods=['POST'])
def delete(date):
    with open('accounting.json') as fj:
            json_record = json.load(fj)
    if date in json_record:
        json_record.pop(date)
        with open('accounting.json', 'w') as fj:
            json.dump(json_record, fj)
        return 'true'
    else:
        return 'false'

@app.route('/test')
def test():
    return render_template('tmp.html')
