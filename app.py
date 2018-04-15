#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request
from msdatabase import mysql_db
from user import User
from info import Info
import json
import os

app = Flask(__name__)

# MySQL
@app.before_request
def _db_connect():
    mysql_db.connect()

@app.teardown_request
def _db_close(exc):
    if not mysql_db.is_closed():
        mysql_db.close()

# API
# 7
@app.route('/api/addUser', methods=['POST'])
def addUser():
    name = request.form.get('name')
    password = request.form.get('password')
    data = {
        "status": "",
        "data":{
            "uid":"",
            "name":"",
            "password":""
        }
    }
    u = User.addUser({
        "name" : name,
        "password": password
    })
    data['data']['uid'] = u.uid
    data['data']['name'] = u.name
    data['data']['password'] = u.password
    data['status'] = True
    return json.dumps(data)

# 6
@app.route('/api/login', methods=['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    data = {
        "status": "",
        "data":{
            "uid":"",
            "name":"",
            "password":""
        }
    }
    u = User.login({
        "name": name,
        "password": password
    })
    if u:
        data['data']['uid'] = u.uid
        data['data']['name'] = u.name
        data['data']['password'] = u.password
        data['status'] = True
    data['status'] = False
    return json.dumps(data)

# 9
@app.route('/api/addSold', methods=['POST'])
def addSold():
    userid = request.form.get('userid')
    title = request.form.get('title')
    details = request.form.get('details')
    price = request.form.get('price')
    tag = request.form.get('tag')
    img = request.files['file']
    img_name = img.filename
    file.save(os.path.join('uploads', img_name))
    data = {
        "status": "",
        "data": {
            "id": "",
            "userid": "",
            "title": "",
            "details": "",
            "price": "",
            "time": "",
            "img_name": "",
            "tag": "",
            "flag": ""
        }
    }
    i = Info.addSold({
        "userid" : userid,
        "title" : title,
        "details": details,
        "price": price,
        "img_name": img_name,
        "tag": tag
    })
    if i:
        data['status'] = True
        data['data']['id'] = i.id
        data['data']['userid'] = i.user
        data['data']['title'] = i.title
        data['data']['details'] = i.details
        data['data']['price'] = i.price
        data['data']['time'] = i.time
        data['data']['img_name'] = i.img_name
        data['data']['tag'] = i.tag
        data['data']['flag'] = i.flag
    else:
        data['status'] = False
    return json.dumps(data)

# 11
@app.route('/api/addBuy', method=['POST'])
def addBuy():
    userid = request.form.get('userid')
    title = request.form.get('title')
    details = request.form.get('details')
    price = request.form.get('price')
    tag = request.form.get('tag')
    data = {
        "status": "",
        "data": {
            "id": "",
            "userid": "",
            "title": "",
            "details": "",
            "price": "",
            "time": "",
            "tag": "",
            "flag": ""
        }
    }
    i = Info.addBuy({
          "userid" : userid,
          "title" : title,
          "details": details,
          "price": price,
          "tag": tag
      })
    if i:
          data['status'] = True
          data['data']['id'] = i.id
          data['data']['userid'] = i.user
          data['data']['title'] = i.title
          data['data']['details'] = i.details
          data['data']['price'] = i.price
          data['data']['time'] = i.time
          data['data']['tag'] = i.tag
          data['data']['flag'] = i.flag
    else:
          data['status'] = False
    return json.dumps(data)

# 1
@app.route('/api/listSold', method=['POST'])
def listSold():
    data = {
        "status" : "",
        "data" : {
        }
    }
    solds = Info.listSold()
    cnt = 0
    for sold in solds:
        data['data'][cnt] = {
            "id" : sold.id,
            "title": sold.title,
            "price": sold.price,
            "time": sold.time
        }
        cnt = cnt + 1
    if cnt==0:
        data['status'] = False
    else:
        data['status'] = True
    return json.dumps(data)

# 3
@app.route('/api/listSoldByTag', method=['POST'])
def listSoldByTag():
    tag = request.form.get('tag')
    data = {
        "status": "",
        "data": {
        }
    }
    solds = Info.listSoldByTag(tag)
    cnt = 0
    for sold in solds:
        data['data'][cnt] = {
            "id" : sold.id,
            "title": sold.title,
            "price": sold.price,
            "time": sold.time
        }
        cnt = cnt + 1
    if cnt==0:
        data['status'] = False
    else:
        data['status'] = True
    return json.dumps(data)

# 4
@app.route('/api/listBuy', method=['POST'])
def listBuy():
    data = {
        "status": "",
        "data": {
        }
    }
    buys = Info.listBuy()
    cnt = 0
    for buy in buys:
        data['data'][cnt] = {
            "id" : buy.id,
            "name": buy.name,
            "tag": buy.tag,
            "title": buy.title
        }
        cnt = cnt + 1
    if cnt==0:
        data['status'] = False
    else:
        data['status'] = True
    return json.dumps(data)
