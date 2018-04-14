#!/usr/bin/env python
# encoding: utf-8
from peewee import *
from msdatabase import *

class Info(BaseModel):
    id = PrimaryKeyField()
    user_id = ForeignKeyField()
    title = CharField()
    details = CharField()
    price = CharField()
    time = DataTimeField()
    img_name = CharField()

    class Meta:
        db_table = 'info'
