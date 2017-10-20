# -*- coding: utf-8 -*-

'''
Created on 2017-10-20 17:40:48
使用SQLAlchemy Core的提取Schema定义功能
@author: zhoujiagen
'''

from sqlalchemy import MetaData
from sqlalchemy_mysql_connection import get_engine

metadata = MetaData()
engine = get_engine()


def _individual_table():
    """处理单个表"""
    from sqlalchemy import Table
    # 自动从后端引擎加载
    users = Table("USERS", metadata, autoload = True, autoload_with = engine)
    for column in  users.columns:
        # 使用>>> dir(Column)查看
        print type(column), column

    # 检查metadata
    t = metadata.tables["USERS"]
    print type(t), t
    print t.foreign_keys  # 外键
    # t.append_constraint() # 添加约束

    # 使用
    from sqlalchemy import select
    s = select([users]).limit(2)
    print type(s), str(s), s.compile().params
    rp = engine.execute(s).fetchall()  # 使用后端引擎执行
    for row in rp:
        print type(row), row

def _whole_database():
    """处理整个数据库"""
    metadata.reflect(engine)
    for table in metadata.sorted_tables:
        print type(table), table


if __name__ == '__main__':
#     _individual_table()
    _whole_database()
