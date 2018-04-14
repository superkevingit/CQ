#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request
from msdatabase import mysql_db
import json

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
