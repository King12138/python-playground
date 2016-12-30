# -*- coding: utf-8 -*-

'''
Created on 2016-12-26 17:02:03
领域实体定义
@author: zhoujiagen
'''
from com.spike.env.log import SpikeConsoleLogger

##############################################################
# ## MySQLdb使用的领域实体
##############################################################
class Entity():
    """实体基类"""
    def __init__(self, ID):
        self.ID = ID

class Employee(Entity):
    """具体实体"""
    def __init__(self, first_name, last_name, age, sex, income):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.income = income

    def __repr__(self):
        if self.id is None:
            return 'Employee[first_name=%s, last_name=%s, age=%d, sex=%c, income=%f]' % (
                self.first_name, self.last_name, self.age, self.sex, self.income)
        else:
            return 'Employee[ID=%d, first_name=%s, last_name=%s, age=%d, sex=%c, income=%f]' % (self.ID,
                self.first_name, self.last_name, self.age, self.sex, self.income)


##############################################################
# ## SQLAlchemy使用的领域实体
##############################################################
logger = SpikeConsoleLogger(logger_name = 'mysql--sqlalchemy-domain').native()

from sqlalchemy.ext.declarative import declarative_base
SQLAlchemy_Base = declarative_base()
from sqlalchemy import Column, BigInteger, Integer, String, CHAR, Float

def create_schema(engine):
    """创建/检查Schema"""
    logger.info('create schema by with engine[%s]' % engine)

    SQLAlchemy_Base.metadata.create_all(engine)


class SQLAlchemy_Employee(SQLAlchemy_Base):
    __tablename__ = 'EMPLOYEE'

    # name为schema中的名称
    id = Column(BigInteger, primary_key = True, autoincrement = True, name = 'ID')
    first_name = Column(String(20), name = 'FIRST_NAME')
    last_name = Column(String(20), name = 'LAST_NAME')
    age = Column(Integer, name = 'AGE')
    sex = Column(CHAR(1), name = 'SEX')
    income = Column(Float, name = 'INCOME')

    def create_schema(self, engine):
        logger.info('create schema by [%s] with engine[%s]' % ('SQLAlchemy_Employee', engine))
        SQLAlchemy_Base.metadata.create_all(engine)

    def __repr__(self):
        if self.id is None:
            return 'Employee[first_name=%s, last_name=%s, age=%d, sex=%c, income=%f]' % (
                self.first_name, self.last_name, self.age, self.sex, self.income)
        else:
            return 'Employee[id=%d, first_name=%s, last_name=%s, age=%d, sex=%c, income=%f]' % (self.id,
                self.first_name, self.last_name, self.age, self.sex, self.income)
