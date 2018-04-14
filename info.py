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
    time = DataTimeField(default=datetime.datetime.now)
    img_name = CharField(null=True)
    tag = CharField() #商品类型 如数码等
    flag = BooleanField(default=0) #商品类型 出售1或收购0

    class Meta:
        db_table = 'info'
