#!/usr/bin/env python
# encoding: utf-8

from peewee import *
from playhouse.pool import PooledMySQLDatabase
import config

mysql_db = PooledMySQLDatabase(config.get('database_db_name'), max_connections=8, stale_timeout=300,
                                                            **{'host': config.get('database_host'),
                                                            'user': config.get('database_user'),
                                                            'password': config.get('database_password'),
                                                            'port': config.get('database_port'),
                                                            'charset': config.get('database_charset')}
                               )

class BaseModel(Model):
    class Meta:
        database = mysql_db
