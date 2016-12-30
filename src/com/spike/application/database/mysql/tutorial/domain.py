# -*- coding: utf-8 -*-

'''
Created on 2016-12-26 17:02:03
领域实体定义
@author: zhoujiagen
'''
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
#=============================================================
# 单个实体
#=============================================================
from sqlalchemy import Column, BigInteger, Integer, String, CHAR, Float
from com.spike.application.database.mysql.tutorial.sqlalchemy_orm_support import SQLAlchemy_Base

class SQLAlchemy_Employee(SQLAlchemy_Base):
    """
CREATE TABLE `EMPLOYEE` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `FIRST_NAME` varchar(20) DEFAULT NULL,
  `LAST_NAME` varchar(20) DEFAULT NULL,
  `AGE` int(11) DEFAULT NULL,
  `SEX` char(1) DEFAULT NULL,
  `INCOME` float DEFAULT NULL,
  PRIMARY KEY (`ID`),
  FULLTEXT KEY `first_name_fulltext` (`FIRST_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

    FULLTEXT search REF: http://stackoverflow.com/questions/14971619/proper-use-of-mysql-full-text-search-with-sqlalchemy
    """
    __tablename__ = 'EMPLOYEE'

    # name为schema中的名称
    id = Column(BigInteger, primary_key = True, autoincrement = True, name = 'ID')
    first_name = Column(String(20), name = 'FIRST_NAME')
    last_name = Column(String(20), name = 'LAST_NAME')
    age = Column(Integer, name = 'AGE')
    sex = Column(CHAR(1), name = 'SEX')
    income = Column(Float, name = 'INCOME')

    def __repr__(self):
        if self.id is None:
            return 'Employee[first_name=%s, last_name=%s, age=%d, sex=%c, income=%f]' % (
                self.first_name, self.last_name, self.age, self.sex, self.income)
        else:
            return 'Employee[id=%d, first_name=%s, last_name=%s, age=%d, sex=%c, income=%f]' % (self.id,
                self.first_name, self.last_name, self.age, self.sex, self.income)

#=============================================================
# 关联的实体
#=============================================================
from sqlalchemy import ForeignKey
from com.spike.application.database.mysql.tutorial.sqlalchemy_orm_support import SQLAlchemy_Relationship_Base
from sqlalchemy.orm import relationship  # 关联

class SQLAlchemy_Relation_Employee(SQLAlchemy_Relationship_Base):
    __tablename__ = 'EMPLOYEES'

    # name为schema中的名称
    id = Column(BigInteger, primary_key = True, autoincrement = True, name = 'ID')
    first_name = Column(String(20), name = 'FIRST_NAME')
    last_name = Column(String(20), name = 'LAST_NAME')
    age = Column(Integer, name = 'AGE')
    sex = Column(CHAR(1), name = 'SEX')
    income = Column(Float, name = 'INCOME')

    dept_id = Column(BigInteger, ForeignKey('DEPARTMENTS.ID'), name = 'DEPT_ID') # 外键 
    department = relationship('SQLAlchemy_Relation_Department', back_populates = 'employees')  # 定义关联

    def __repr__(self):
        if self.id is None:
            return 'Employee[first_name=%s, last_name=%s, age=%d, sex=%c, income=%f]' % (
                self.first_name, self.last_name, self.age, self.sex, self.income)
        else:
            return 'Employee[id=%d, first_name=%s, last_name=%s, age=%d, sex=%c, income=%f]' % (self.id,
                self.first_name, self.last_name, self.age, self.sex, self.income)

class SQLAlchemy_Relation_Department(SQLAlchemy_Relationship_Base):
    __tablename__ = 'DEPARTMENTS'

    id = Column(BigInteger, primary_key = True, autoincrement = True, name = 'ID')
    name = Column(String(50), name = "NAME")

# 定义关联
SQLAlchemy_Relation_Department.employees = relationship(
    'SQLAlchemy_Relation_Employee',
    order_by = SQLAlchemy_Employee.id,
    back_populates = 'department')
