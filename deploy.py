#!/usr/bin/env python
# encoding: utf-8
from user import *
from info import *

mysql_db.connect()

if( u'user' not in mysql_db.get_tables() ):
    mysql_db.create_table(User)

if( u'info' not in mysql_db.get_tables() ):
    mysql_db.create_table(Info)

mysql_db.close()

