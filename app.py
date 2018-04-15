#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request, send_from_directory
from werkzeug import secure_filename
import json
import os

from ms_database import mysql_db
from user import User
from info import Info

BASEPATH = os.path.dirname(__file__)
UPLOAD_PATH = os.path.join(BASEPATH, 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_PATH'] = UPLOAD_PATH

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
    tel = request.form.get('tel')
    data = {
        "status": "",
        "data":{
            "uid":"",
            "name":"",
            "password":"",
            "tel":""
        }
    }
    u = User.addUser({
        "name" : name,
        "password": password,
        "tel": tel
    })
    data['data']['uid'] = u.uid
    data['data']['name'] = u.name
    data['data']['password'] = u.password
    data['data']['tel'] = u.tel
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
    else:
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
    file = request.files['img_file']
    img_name = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_PATH'], img_name))
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
        data['data']['time'] = i.time.strftime('%Y-%m-%d %H:%M:%S')
        data['data']['img_name'] = i.img_name
        data['data']['tag'] = i.tag
        data['data']['flag'] = i.flag
    else:
        data['status'] = False
    return json.dumps(data)

# 11
@app.route('/api/addBuy', methods=['POST'])
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
          data['data']['time'] = i.time.strftime('%Y-%m-%d %H:%M:%S')
          data['data']['tag'] = i.tag
          data['data']['flag'] = i.flag
    else:
          data['status'] = False
    return json.dumps(data)

# 1
@app.route('/api/listSold', methods=['POST'])
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
            "time": sold.time.strftime('%Y-%m-%d %H:%M:%S')
        }
        cnt = cnt + 1
    if cnt==0:
        data['status'] = False
    else:
        data['status'] = True
    return json.dumps(data)

# 3
@app.route('/api/listSoldByTag', methods=['POST'])
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
            "time": sold.time.strftime('%Y-%m-%d %H:%M:%S')
        }
        cnt = cnt + 1
    if cnt==0:
        data['status'] = False
    else:
        data['status'] = True
    return json.dumps(data)

# 8
@app.route('/api/listSoldByUserid', methods=['POST'])
def listSoldByUserid():
    uid = request.form.get('userid')
    data = {
        "status": "",
        "data": {
        }
    }
    solds = Info.listSoldByUserid(uid)
    cnt = 0
    for sold in solds:
        data['data'][cnt] = {
            "id" : sold.id,
            "title": sold.title,
            "price": sold.price,
            "time": sold.time.strftime('%Y-%m-%d %H:%M:%S')
        }
        cnt = cnt + 1
    if cnt==0:
        data['status'] = False
    else:
        data['status'] = True
    return json.dumps(data)

# 4
@app.route('/api/listBuy', methods=['POST'])
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
            "name": buy.user.name,
            "tag": buy.tag,
            "title": buy.title
        }
        cnt = cnt + 1
    if cnt==0:
        data['status'] = False
    else:
        data['status'] = True
    return json.dumps(data)

# 10
@app.route('/api/listBuyByUserid', methods=['POST'])
def listBuyByUserid():
    uid = request.form.get('userid')
    data = {
        "status": "",
        "data": {
        }
    }
    buys = Info.listBuyByUserid(uid)
    cnt = 0
    for buy in buys:
        data['data'][cnt] = {
            "id" : buy.id,
            "name": buy.user.name,
            "tag": buy.tag,
            "title": buy.title
        }
        cnt = cnt + 1
    if cnt==0:
        data['status'] = False
    else:
        data['status'] = True
    return json.dumps(data)

# 2
@app.route('/api/listSoldDetails', methods=['POST'])
def listSoldDetails():
    id = request.form.get('id')
    d = Info.listSoldDetails(id)
    data = {
        "status" : "",
        "data":{
            "id" : "",
            "name" : "",
            "tel" : "",
            "details" : "",
            "img_name" : "",
            "time" : ""
        }
    }
    if not d:
        data['status'] = False
    else:
        data['status'] = True
        data['data']['id'] = d.id
        data['data']['name'] = d.user.name
        data['data']['tel'] = d.user.tel
        data['data']['details'] = d.details
        data['data']['img_name'] = d.img_name
        data['data']['time'] = d.time.strftime('%Y-%m-%d %H:%M:%S')
    return json.dumps(data)

# 5
@app.route('/api/listBuyDetails', methods=['POST'])
def listBuyDetails():
    id = request.form.get('id')
    d = Info.listBuyDetails(id)
    data = {
        "status" : "",
        "data":{
            "id" : "",
            "name" : "",
            "tel" : "",
            "details" : "",
            "price" : "",
            "time" : ""
        }
    }
    if not d:
        data['status'] = False
    else:
        data['status'] = True
        data['data']['id'] = d.id
        data['data']['name'] = d.user.name
        data['data']['tel'] = d.user.tel
        data['data']['details'] = d.details
        data['data']['price'] = d.price
        data['data']['time'] = d.time.strftime('%Y-%m-%d %H:%M:%S')
    return json.dumps(data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'],
                               filename)
