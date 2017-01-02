# -*- coding: utf-8 -*-

'''
Created on 2016-12-26 16:45:29
SQLAlchemy ORM教程 - 单个实体

资源:
[SQLAlchemy 1.1 Documentation - Object Relational Tutorial](http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html)
@author: zhoujiagen
'''
import time

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from com.spike.application.database.mysql.tutorial.domain import SQLAlchemy_Employee as Employee
from com.spike.application.database.mysql.tutorial.sqlalchemy_orm_support import SQLAlchemy_Base
import com.spike.application.database.mysql.tutorial.sqlalchemy_orm_support as SQLAlchemyOrmTutorialSupport
from com.spike.env.log import SpikeConsoleLogger


logger = SpikeConsoleLogger('SQLAlchemy-ORM-Tutorial').native()


# 计时参考: http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python

def new_transient_entity(first_name = 'Eric', last_name = 'Cartman', age = 10, sex = 'M', income = 10000.0):
    """5 创建映射类实例"""
    employee = Employee(
            first_name = first_name,
            last_name = last_name,
            age = age,
            sex = sex,
            income = income)

    return employee


def _queries(session):
    """
    简单查询示例
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

def _query_common_filter_opearators(session):
    """常见的过滤操作:
    equals/not equals, like, in/not in, is null/is not null, and, or, match
    """

    start = time.time()

    query = session.query(Employee)

    print '-' * 200
    results = query.filter(Employee.first_name == 'Eric2').all()  # equals
    for row in results:
        logger.info(row)

    print '-' * 200
    results = query.filter(Employee.first_name != 'Eric2').all()  # not equals
    for row in results:
        logger.info(row)

    print '-' * 200
    results = query.filter(Employee.first_name.like('%2')).all()  # like
    for row in results:
        logger.info(row)

    print '-' * 200
    results = query.filter(Employee.first_name.in_(['Eric0', 'Eric2']))  # in
    for row in results:
        logger.info(row)

    print '-' * 200
    results = query.filter(~Employee.first_name.in_(['Eric0', 'Eric2']))  # not in
    for row in results:
        logger.info(row)

    print '-' * 200
    results = query.filter(Employee.first_name == None)  # is null
    for row in results:
        logger.info(row)

    print '-' * 200
    results = query.filter(Employee.first_name != None)  # is not null
    for row in results:
        logger.info(row)

    # and
    # (1) 使用and_()
    print '-' * 200
    from sqlalchemy import and_
    results = query.filter(and_(Employee.first_name == 'Eric0', Employee.last_name == 'Cartman'))
    for row in results:
        logger.info(row)
    # (2) filter()中使用多个表达式
    print '-' * 200
    results = query.filter(Employee.first_name == 'Eric0', Employee.last_name == 'Cartman')
    for row in results:
        logger.info(row)
    # (3) 链式调用filter()/filter_by()
    print '-' * 200
    results = query.filter(Employee.first_name == 'Eric0').filter(Employee.last_name == 'Cartman')
    for row in results:
        logger.info(row)

    # or
    print '-' * 200
    from sqlalchemy import or_
    results = query.filter(or_(Employee.first_name == 'Eric0', Employee.last_name == 'Cartman2'))
    for row in results:
        logger.info(row)

    # match
    # full text index: ALTER TABLE `test`.`EMPLOYEE`
    #     ADD FULLTEXT INDEX `first_name_fulltext` (`FIRST_NAME` ASC);
    print '-' * 200
    # WHERE MATCH (`EMPLOYEE`.first_name) AGAINST (%s IN BOOLEAN MODE)
    results = query.filter(Employee.first_name.match('+Eric0'))
    for row in results:
        logger.info(row)

    end = time.time()
    print 'last %s seconds' % (end - start)

def _query_returning_list_and_scalar(session):
    """Query上的方法: 返回列表和标量"""
    start = time.time()
    print '-' * 200
    query = session.query(Employee).filter(Employee.first_name == 'Eric0').order_by(Employee.id)
    logger.info(query.all())  # all()

    print '-' * 200
    logger.info(query.first())  # first()

    # one()
    print '-' * 200
    try:
        query.one()
    except MultipleResultsFound as e:  # 返回多个结果
        logger.error(e)
    try:
        session.query(Employee).filter(Employee.id == -1).one()
    except NoResultFound as e:  # 无结果返回
        logger.error(e)

    print '-' * 200
    # one_or_none()
    logger.info(session.query(Employee).filter(Employee.id == -1).one_or_none())

    # scalar(): 调用one(), 成功时返回第一列元素(WRONG!!!)
    query = session.query(Employee).filter(Employee.id == 12)  # id=12可能需要修改
    logger.info(query.one())
    logger.info(query.scalar())

    end = time.time()
    print 'last %s seconds' % (end - start)

def _query_using_texual_sql(session):
    """使用文本SQL"""

    from sqlalchemy import text

    start = time.time()
    print '-' * 200
    # (1) 不带参数
    results = session.query(Employee).filter(text('id<13')).all()
    for row in results:
        logger.info(row)

    print '-' * 200
    # (2) 带参数
    results = session.query(Employee). \
        filter(text('id<:id_value and first_name=:first_name_value')). \
        params(id_value = 13, first_name_value = 'Eric0').all()
    for row in results:
        logger.info(row)

    print '-' * 200
    # (3) 使用原生SQL: from_statement()
    results = session.query(Employee).\
        from_statement(text("SELECT * FROM EMPLOYEE WHERE first_name = :first_name_value")). \
        params(first_name_value = 'Eric0').all()
    for row in results:
        logger.info(row)
    print '-' * 200
    # 绑定原生SQL中schema字段与映射属性的对应关系
    stmt = text('SELECT FIRST_NAME, ID,AGE,SEX,INCOME, LAST_NAME FROM EMPLOYEE WHERE FIRST_NAME=:first_name_value')
    stmt = stmt.columns(Employee.first_name, Employee.id, Employee.age, Employee.sex, Employee.income, Employee.last_name)
    results = session.query(Employee).from_statement(stmt).\
        params(first_name_value = 'Eric0').all()
    for row in results:
        logger.info(row)

    end = time.time()
    print 'last %s seconds' % (end - start)

def _query_counting(session):
    """统计"""

    start = time.time()

    print '-' * 200
    count = session.query(Employee).filter(Employee.first_name == 'Eric0').count()
    logger.info(count)

    # 使用func(): group by
    print '-' * 200
    from sqlalchemy import func
    results = session.query(func.count(Employee.first_name), Employee.first_name).group_by(Employee.first_name).all()
    for row in results:
        logger.info(row)

    end = time.time()
    print 'last %s seconds' % (end - start)

if __name__ == '__main__':
    # 1 检查版本
    SQLAlchemyOrmTutorialSupport.show_version()

    # 2 建立连接
    engine = SQLAlchemyOrmTutorialSupport.create_engine()

    # 3 声明映射见SQLAlchemy_Employee

    # 4 创建Schema
    SQLAlchemyOrmTutorialSupport.create_schema(engine, SQLAlchemy_Base)
    # 创建全文索引, 只需要执行一次
    #SQLAlchemyOrmTutorialSupport.create_mysql_fulltext_index(engine)

    # 5 创建映射类实例
    employee = new_transient_entity()
    logger.info(str(employee.id))  # None

    # 6 创建Session
    session = SQLAlchemyOrmTutorialSupport.create_session(engine)

    # 7 创建和更新对象
# commented for query
    session.add(employee)  # 加入transient实体
    logger.info(employee.id)  # None, pending(not flushed)
    logger.info('session.new=%s', session.new)

    employee_ = session.query(Employee).filter_by(first_name = 'Eric').first()  # 查询
    employee_.first_name = 'Eric0'
    logger.info('employee_ is employee: %s', employee_ is employee)
    logger.info('session.dirty=%s', session.dirty)

    employees = [new_transient_entity(first_name = 'Eric2', last_name = 'Cartman2', age = 10, sex = 'M', income = 10000.0),
                 new_transient_entity(first_name = 'Eric3', last_name = 'Cartman3', age = 10, sex = 'M', income = 10000.0)]
    session.add_all(employees)  # 加入多个transient实体

    logger.info('session.new=%s', session.new)
    logger.info('session.dirty=%s', session.dirty)

    # 提交会话事务
    session.commit()
    # 查看ID
    logger.info(employee_.id) # 事务提交后才可以查询出新建记录的id
    for e in employees:
        logger.info(e.id)

    # 8 回滚
    employee_for_rollback = new_transient_entity('Eric4', 'Cartman4')
    session.add(employee_for_rollback)
    logger.info('employee_for_rollback in session? %s', employee_for_rollback in session)
    logger.info(session.query(Employee).filter(Employee.first_name.in_(['Eric4'])).all())
    session.rollback()
    logger.info('employee_for_rollback in session? %s', employee_for_rollback in session)
    logger.info(session.query(Employee).filter(Employee.first_name.in_(['Eric4'])).all())

    # 9 查询
    # _queries(session)
    _query_common_filter_opearators(session)
    _query_returning_list_and_scalar(session)
    _query_using_texual_sql(session)
    _query_counting(session)

    session.close_all()

