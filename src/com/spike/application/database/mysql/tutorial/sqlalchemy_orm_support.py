# -*- coding: utf-8 -*-

'''
Created on 2016-12-30 18:37:08
SQLAlchemy ORM支持性模块
@author: zhoujiagen
'''

import sqlalchemy

from com.spike.env.log import SpikeConsoleLogger
logger = SpikeConsoleLogger('SQLAlchemy-ORM-Tutorial-Support').native()


def show_version():
    """检查版本"""
    logger.info('Framework version is: %s' % sqlalchemy.__version__)

def create_engine():
    """建立连接"""
    engine = sqlalchemy.create_engine('mysql://root:@localhost/test', echo = True)
    logger.info('create engine: %s' % engine)
    return engine

from sqlalchemy.ext.declarative import declarative_base
SQLAlchemy_Base = declarative_base()  # 单个实体
SQLAlchemy_Relationship_Base = declarative_base()  # 多个实体, 带关系

def create_schema(engine, base = SQLAlchemy_Base):
    """创建/检查Schema"""
    logger.info('create schema by with engine[%s], base[%s]' % (engine, base))

    base.metadata.create_all(engine)

from sqlalchemy.orm.session import sessionmaker

def create_session(engine):
    """创建Session"""
    Session = sessionmaker(bind = engine)  # 使用session工厂
    session = Session()  # session实例
    return session

def create_mysql_fulltext_index(base=SQLAlchemy_Base):
    """
    TODO: 创建MySQL全文索引
    REF http://stackoverflow.com/questions/14971619/proper-use-of-mysql-full-text-search-with-sqlalchemy
    """
    connect = base.metadata.bind.connect()
    connect.execute('CREATE FULLTEXT INDEX first_name_fulltext ON EMPLOYEE (FIRST_NAME ASC)')



if __name__ == '__main__':
    pass
