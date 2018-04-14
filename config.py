#!/usr/bin/env python
# encoding: utf-8

settings = {
    # 数据库配置
    "database_db_name" : "",
    "database_host" : "localhost",
    "database_user" : "",
    "database_password" : "",
    "database_port" : 3306,
    "database_charset": "utf8",
}

def get(str):
    return settings[str]
