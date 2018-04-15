#!/usr/bin/env python
# encoding: utf-8
from peewee import *
from msdatabase import *

class User(BaseModel):
    uid = PrimaryKeyField()
    name = CharField()
    password = CharField()
    tel = CharField()

    class Meta:
        db_table = 'user'

    # 没有验证是否重名
    @classmethod
    def addUser(cls, info):
        u = cls.create(
            name = info['name'],
            password = info['password'],
            tel = info['tel']
        )
        return u

    @classmethod
    def login(cls, info):
        u = cls.select().where(cls.name==info['name'])
        for n in u:
            if n.password==info['password']:
                return n
        return False
