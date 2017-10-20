# -*- coding: utf-8 -*-

'''
Created on 2017-10-19 17:37:44
SQLAlchemy MySQL连接
@author: zhoujiagen
'''

from sqlalchemy import create_engine

def get_engine(host = 'localhost', user = 'root', passwd = 'root', db = 'test', port = 3306):
    """获取后端存储引擎"""
    connect_string = "mysql+mysqldb://%s:%s@%s:%s/%s" % (user, passwd, host, port, db)
    engine = create_engine(connect_string, pool_recycle = 3600)
    return engine

def get_connection_through_engine(engine = None):
    """通过后端存储引擎获取数据库连接"""
    return engine.connect()

def get_connection(host = 'localhost', user = 'root', passwd = 'root', db = 'test', port = 3306):
    """获取数据库连接"""
    engine = get_engine(host, user, passwd, db, port)
    connection = engine.connect()
    return connection


if __name__ == '__main__':
#     # mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
#     connect_string = "mysql+mysqldb://root:root@localhost:3306/test"
#     engine = create_engine(connect_string, pool_recycle = 3600)
#     connection = engine.connect()
    connection = get_connection()
    print connection

