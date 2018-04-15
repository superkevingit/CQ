#!/usr/bin/env python
# encoding: utf-8
from peewee import *
from ms_database import *
from user import User
from datetime import datetime

class Info(BaseModel):
    id = PrimaryKeyField()
    user = CharField()
    title = CharField()
    details = CharField()
    price = CharField()
    time = DateTimeField(default=datetime.now)
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
        l = cls.select().where(cls.flag==1)
        return l

    @classmethod
    def listSoldByTag(cls, tag):
        l = cls.select().where(cls.tag == tag, cls.flag==1)
        return l

    @classmethod
    def listSoldByUserid(cls, uid):
        l = cls.select().where(cls.user == uid, cls.flag==1)
        return l

    @classmethod
    def listBuy(cls):
        l = cls.select().join(User).where(User.uid == cls.user, cls.flag==0)
        return l

    @classmethod
    def listBuyByUserid(cls, uid):
        l = cls.select().join(User).where(User.uid == cls.user, cls.user == uid, cls.flag==0)
        return l

    @classmethod
    def listSoldDetails(cls, id):
        ds = cls.select().join(User).where(cls.id==id ,User.uid == cls.user)
        for d in ds:
            return d
    @classmethod
    def listBuyDetails(cls, id):
        ds = cls.select().join(User).where(cls.id==id ,User.uid == cls.user)
        for d in ds:
            return d





