# -*- coding: utf-8 -*-

'''
Created on 2017-10-19 16:08:19
MySQLdb基本操作
[MySQL-python 1.2.5 - PyPi](https://pypi.python.org/pypi/MySQL-python/1.2.5)

执行SQL: 
row_cnt = cursor.execute(sql), data = cursor.fetchone(), results = cursor.fetchall()
执行/回滚事务: 
db.commit(), db.rollback()
获取自动生成的ID: (REF http://stackoverflow.com/questions/2548493/how-do-i-get-the-id-after-insert-into-mysql-database-with-python)
cursor.lastrowid
@author: zhoujiagen
'''

import MySQLdb

def Open(host = 'localhost', user = 'root', passwd = 'root', db = 'test', port = 3306):
    """返回建立的连接"""
    conn = MySQLdb.connect(host = host, user = user, passwd = passwd, db = db, port = port)
    return conn

def Close(conn):
    """关闭廉价"""
    conn.close()

def CreateSchema(conn, schemaSql = None):
    """"Schema操作"""
    if  schemaSql is None: return
    conn.cursor().execute(schemaSql)

def Insert(conn, insertSql = None):
    """插入操作"""
    if insertSql is None: return

    cursor = conn.cursor();
    try:
        cursor.execute(insertSql)
        rowid = cursor.lastrowid
        conn.commit()
    except:
        conn.rollback()

    return rowid

def Update(conn, updateSql):
    """更新操作"""
    _Execute(conn, updateSql)

def Delete(conn, deleteSql):
    """删除操作"""
    _Execute(conn, deleteSql)

def _Execute(conn, sql = None):
    if sql is None: return

    cursor = conn.cursor();
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

def Query(conn, querySql):
    """查询操作, 返回字段元组的列表"""
    if querySql is None: return

    cursor = conn.cursor()
    cursor.execute(querySql)
    return cursor.fetchall()

if __name__ == '__main__':
    ######################################################
    conn = Open()
    print conn

    ######################################################
    schema_sql = """
    CREATE TABLE `EMPLOYEE` (
              `ID` BIGINT NOT NULL AUTO_INCREMENT,
              `FIRST_NAME` VARCHAR(20) NULL,
              `LAST_NAME` VARCHAR(20) NULL,
              `AGE` INT NULL,
              `SEX` CHAR(1) NULL,
              `INCOME` FLOAT NULL,
              PRIMARY KEY (`ID`))
    """
    CreateSchema(conn, "DROP TABLE IF EXISTS `EMPLOYEE`")
    CreateSchema(conn, schema_sql)

    ######################################################
    insert_sql_template = """INSERT INTO `EMPLOYEE` (`FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`)  
        VALUES ('%s', '%s', '%d', '%c', '%f')"""
    records = [
        ('Alice', 'Cartman', 10, '0', 10000),
        ('Bob', 'Cartman', 20, '0', 20000),
        ('Cart', 'Cartman', 30, '1', 30000),
        ('David', 'Cartman', 40, '1', 40000),
        ('Eric', 'Cartman', 50, '0', 50000),
    ]
    # insert_sql = insert_sql_template % ('Eric', 'Cartman', 10, '0', 10000)
    rowids = [Insert(conn, insert_sql_template % record) for record in records]
    print rowids
    print Query(conn, "SELECT * FROM EMPLOYEE")

    ######################################################
    Update(conn, "UPDATE EMPLOYEE SET sex = 'M' WHERE sex = '0'")
    print Query(conn, "SELECT * FROM EMPLOYEE")

    ######################################################
    Delete(conn, "DELETE FROM EMPLOYEE WHERE sex = 'M'")
    print Query(conn, "SELECT * FROM EMPLOYEE")

    ######################################################
    print Query(conn, "SELECT * FROM EMPLOYEE WHERE ID = -1")  # 返回()

    ######################################################
    Close(conn)



