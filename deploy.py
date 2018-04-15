#!/usr/bin/env python
# encoding: utf-8
from ms_database import mysql_db
from user import User
from info import Info

mysql_db.connect()

if( u'user' not in mysql_db.get_tables() ):
    User.create_table()

if( u'info' not in mysql_db.get_tables() ):
    Info.create_table()

mysql_db.close()

