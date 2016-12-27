# -*- coding: utf-8 -*-

'''
Created on 2016-12-26 16:45:29
SQLAlchemy ORM教程

资源:
[SQLAlchemy 1.1 Documentation - Object Relational Tutorial](http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html)
@author: zhoujiagen
'''
from com.spike.env.log import SpikeConsoleLogger
logger = SpikeConsoleLogger('SQLAlchemy-ORM-Tutorial').native()

import sqlalchemy

from com.spike.application.database.mysql.tutorial.domain import SQLAlchemy_Employee as Employee
from sqlalchemy.orm.session import sessionmaker

def show_version():
    """1 检查版本"""
    # 1 检查版本
    logger.info('Framework version is: %s' % sqlalchemy.__version__)

def create_engine():
    """2 建立连接"""
    engine = sqlalchemy.create_engine('mysql://root:@localhost/test', echo = True)
    return engine

def new_transient_entity(first_name = 'Eric', last_name = 'Cartman', age = 10, sex = 'M', income = 10000.0):
    """5 创建映射类实例"""
    employee = Employee(
            first_name = first_name,
            last_name = last_name,
            age = age,
            sex = sex,
            income = income)

    return employee


def create_session(engine):
    """6 创建Session"""
    Session = sessionmaker(bind = engine)  # 使用session工厂
    session = Session()  # session实例
    return session

def _queries(session):
    # 计时参考: http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
    import time
    """
    查询示例
    session.query()返回Query对象, 其方法参数可以是类和类装配描述符
    
    """
    print '-' * 200
    start = time.time()
    # 查询整个EMPLOYEE表, 按id降序排序(降序参考http://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending)
    for instance in session.query(Employee).order_by(Employee.id.desc()):
        logger.info(instance)
    end = time.time()
    print 'last %s seconds' % (end - start)

    print '-' * 200
    start = time.time()
    # 查询整个EMPLOYEE表, 选择了返回字段,  结果为tuple
    for first_name, last_name in session.query(Employee.first_name, Employee.last_name):
        logger.info('first_name=%s, last_name=%s', first_name, last_name)
    end = time.time()
    print 'last %s seconds' % (end - start)

    print '-' * 200
    start = time.time()
    # 混合使用类和类装配描述符
    for row in session.query(Employee, Employee.first_name).all():
        logger.info("Employee=%s, first_name=%s", row[0], row.first_name)
    end = time.time()
    print 'last %s seconds' % (end - start)

    # alias被略去

    print '-' * 200
    start = time.time()
    # 过滤操作: filter_by, filter
    # like查询: REF http://stackoverflow.com/questions/3325467/elixir-sqlalchemy-equivalent-to-sql-like-statement
    for first_name, last_name in session.query(Employee.first_name, Employee.last_name).filter(Employee.last_name.like('%2%')):
        logger.info('first_name=%s, last_name=%s', first_name, last_name)
    for e in session.query(Employee).filter_by(last_name = 'Eric3'):  # 注意是=
        logger.info('first_name=%s, last_name=%s', e.first_name, e.last_name)
    for e in session.query(Employee).filter(Employee.last_name == 'Eric4'):  # 注意是==
        logger.info('first_name=%s, last_name=%s', e.first_name, e.last_name)
    end = time.time()
    print 'last %s seconds' % (end - start)

    print '-' * 200
    start = time.time()
    end = time.time()
    print 'last %s seconds' % (end - start)

    print '-' * 200
    start = time.time()
    end = time.time()
    print 'last %s seconds' % (end - start)

    print '-' * 200
    start = time.time()
    end = time.time()
    print 'last %s seconds' % (end - start)

    print '-' * 200

if __name__ == '__main__':
    engine = create_engine()
    logger.info(engine)

    # 3 声明映射见SQLAlchemy_Employee

    # 4 创建Schema
# commented for query
#    create_schema(engine)

    # 5 创建映射类实例
    employee = new_transient_entity()
    logger.info(str(employee.id))  # None

    session = create_session(engine)

    # 7 创建和更新对象
# commented for query
#     session.add(employee)  # 加入transient实体
#     logger.info(employee.id)  # None, pending(not flushed)
#     logger.info('session.new=%s', session.new)
#
#     employee_ = session.query(Employee).filter_by(first_name = 'Eric').first()  # 查询
#     employee_.first_name = 'Eric0'
#     logger.info('employee_ is employee: %s', employee_ is employee)
#     logger.info('session.dirty=%s', session.dirty)
#
#     employees = [new_transient_entity(first_name = 'Eric2', last_name = 'Cartman2', age = 10, sex = 'M', income = 10000.0),
#                  new_transient_entity(first_name = 'Eric3', last_name = 'Cartman3', age = 10, sex = 'M', income = 10000.0)]
#     session.add_all(employees)  # 加入多个transient实体
#
#     logger.info('session.new=%s', session.new)
#     logger.info('session.dirty=%s', session.dirty)
#
#     # 提交会话事务
#     session.commit()
#     # 查看ID
#     logger.info(employee_.id)
#     for e in employees:
#         logger.info(e.id)

    # 8 回滚
    employee_for_rollback = new_transient_entity('Eric4', 'Cartman4')
    session.add(employee_for_rollback)
    logger.info('employee_for_rollback in session? %s', employee_for_rollback in session)
    logger.info(session.query(Employee).filter(Employee.first_name.in_(['Eric4'])).all())
    session.rollback()
    logger.info('employee_for_rollback in session? %s', employee_for_rollback in session)
    logger.info(session.query(Employee).filter(Employee.first_name.in_(['Eric4'])).all())

    # 9 查询
    _queries(session)

