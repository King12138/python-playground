# -*- coding: utf-8 -*-  

'''
Created on 2016-12-28 16:41:55
SQLAlchemy ORM教程 - 多个实体

资源:
[SQLAlchemy 1.1 Documentation - Object Relational Tutorial](http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html)
@author: zhoujiagen
'''

from com.spike.application.database.mysql.tutorial.domain import SQLAlchemy_Relation_Department as Department, \
    SQLAlchemy_Relation_Employee as Employee
from com.spike.application.database.mysql.tutorial.sqlalchemy_orm_support import SQLAlchemy_Relationship_Base
import com.spike.application.database.mysql.tutorial.sqlalchemy_orm_support as SQLAlchemyOrmTutorialSupport


if __name__ == '__main__':
    
    SQLAlchemyOrmTutorialSupport.show_version()
    engine = SQLAlchemyOrmTutorialSupport.create_engine()
    SQLAlchemyOrmTutorialSupport.create_schema(engine, SQLAlchemy_Relationship_Base)
    
    session = SQLAlchemyOrmTutorialSupport.create_session(engine)
    department = Department(name="IT")
    employee = Employee(first_name = 'Eric', last_name = 'Cartman', age = 10, sex = 'M', income = 10000.0, department=department)
    session.add(employee)
    
    # 第一次提交事务才真正创建schema
    session.commit()
    
    # 10 构建和使用关系

    # 11 联接查询

    # 12 贪婪加载

    # 13 级联删除

    # 14 构建多对多关系
    
    pass