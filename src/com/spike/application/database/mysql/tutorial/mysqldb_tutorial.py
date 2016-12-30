# -*- coding: utf-8 -*-

'''
Created on 2016-12-26 11:42:33
MySQLdb教程

执行SQL: 
row_cnt = cursor.execute(sql), data = cursor.fetchone(), results = cursor.fetchall()
执行/回滚事务: 
db.commit(), db.rollback()
获取自动生成的ID: (REF http://stackoverflow.com/questions/2548493/how-do-i-get-the-id-after-insert-into-mysql-database-with-python)
cursor.lastrowid

参考资料:
[python操作mysql数据库 - 菜鸟教程  runoob.com](http://www.runoob.com/python/python-mysql.html)
[Python连接MySQL数据库 - 简书](http://www.jianshu.com/p/76fab6cb06f9)
[MySQL-python 1.2.5 - PyPi](https://pypi.python.org/pypi/MySQL-python/1.2.5)
@author: zhoujiagen
'''
import MySQLdb

from com.spike.application.database.mysql.tutorial.domain import Employee


def establish_database_connection():
    """数据库连接"""
    # 开启连接
    db = MySQLdb.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db = 'test',
        port = 3306)

    cursor = db.cursor()  # 操作游标
    cursor.execute('SELECT VERSION()')  # 执行查询
    data = cursor.fetchone()

    print 'database version is %s' % data
    # database version is 5.6.34

    # 关闭连接
    db.close()


def create_schema():
    """创建数据库表"""
    db = MySQLdb.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db = 'test',
        port = 3306)
    cursor = db.cursor()

    # 不存在时会跑出warning
    cursor.execute('DROP TABLE IF EXISTS `EMPLOYEE`')

    sql = """
            CREATE TABLE `EMPLOYEE` (
              `ID` BIGINT NOT NULL AUTO_INCREMENT,
              `FIRST_NAME` VARCHAR(20) NULL,
              `LAST_NAME` VARCHAR(20) NULL,
              `AGE` INT NULL,
              `SEX` CHAR(1) NULL,
              `INCOME` FLOAT NULL,
              PRIMARY KEY (`ID`))
    """
    cursor.execute(sql)

    db.close()

def insert_operation():
    """插入操作"""
    db = MySQLdb.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db = 'test',
        port = 3306)
    cursor = db.cursor()
    sql = """
            INSERT INTO `EMPLOYEE` (`FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`) 
            VALUES ('Eric', 'Cartman', '10', '0', '10000')
    """

    # sql模板
    sql_template = """INSERT INTO `EMPLOYEE` (`FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`)  
        VALUES ('%s', '%s', '%d', '%c', '%f')""" % ('Eric', 'Cartman', 10, '0', 10000)

    try:
        cursor.execute(sql)
        # 获取自动生成的ID, REF http://stackoverflow.com/questions/2548493/how-do-i-get-the-id-after-insert-into-mysql-database-with-python
        print 'ID=%s' % cursor.lastrowid
        cursor.execute(sql_template)
        print 'ID=%s' % cursor.lastrowid
        db.commit()  # 提交
    except:
        db.rollback()  # 回滚

    db.close()

def query_operation():
    """查询操作"""
    db = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            db = 'test',
            port = 3306)
    cursor = db.cursor()

    sql = "SELECT * FROM EMPLOYEE WHERE INCOME >= 800.0"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()  # 获取所有记录列表
        for row in results:
            # print row
            employee = Employee(row[1], row[2], int(row[3]), row[4], float(row[5]))
            employee.ID = int(row[0])
            print employee
    except Exception as e:
        print 'Error: Unable to fetch data:', e

    db.close()

def update_operation():
    """更新操作"""
    db = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            db = 'test',
            port = 3306)
    cursor = db.cursor()

    sql = "UPDATE EMPLOYEE SET sex = 'M' WHERE sex = '0'"
    try:
        row_cnt = cursor.execute(sql)
        db.commit()
        print 'row_cnt = %d' % row_cnt
    except:
        db.rollback()

    db.close()

def delete_operation():
    """删除操作"""
    db = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            db = 'test',
            port = 3306)
    cursor = db.cursor()

    sql = "DELETE FROM EMPLOYEE WHERE sex = 'M'"
    try:
        row_cnt = cursor.execute(sql)
        db.commit()
        print 'row_cnt = %d' % row_cnt
    except:
        db.rollback()

    db.close()

if __name__ == '__main__':
    establish_database_connection()
    create_schema()
    insert_operation()
    query_operation()
    update_operation()
    delete_operation()
