#!/usr/bin/env python
# encoding: utf-8

settings = {
    # 数据库配置
    "database_db_name" : "cq",
    "database_host" : "localhost",
    "database_user" : "root",
    "database_password" : "",
    "database_port" : 3306,
    "database_charset": "utf8",
}

def get(str):
    return settings[str]
