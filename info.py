#!/usr/bin/env python
# encoding: utf-8
from peewee import *
from msdatabase import *
from user import User

class Info(BaseModel):
    id = PrimaryKeyField()
    user = CharField()
    title = CharField()
    details = CharField()
    price = CharField()
    time = DataTimeField(default=datetime.datetime.now)
    img_name = CharField(null=True)
    tag = CharField() #商品类型 如数码等
    flag = BooleanField(default=0) #商品类型 出售1或收购0

    class Meta:
        db_table = 'info'

    @classmethod
    def addSold(cls, info):
        i = cls.create(
            user = info['userid'],
            title = info['title'],
            details = info['details'],
            price = info['price'],
            img_name = info['img_name'],
            tag = info['tag'],
            flag = 1
        )
        return i

    @classmethod
    def addBuy(cls, info):
        i = cls.create(
            user = info['userid'],
            title = info['title'],
            details = info['details'],
            price = info['price'],
            tag = info['tag'],
            flag = 0
        )
        return i

    @classmethod
    def listSold(cls):
        l = cls.select(id, title, price, time)
        return l

    @classmethod
    def listSoldByTag(cls, tag):
        l = cls.select(id, title, price, time).where(cls.tag == tag)
        return l

    @classmethod
    def listBuy(cls):
        l = cls.select(id, title, tag, name).join(User).where(User.uid == cls.user)
        return l
