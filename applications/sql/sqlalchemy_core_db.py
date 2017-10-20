# -*- coding: utf-8 -*-

'''
Created on 2017-10-20 10:12:15
使用SQLAlchemy Core的数据库操作模块(Schema定义和连接等)
@author: zhoujiagen
'''
from datetime import datetime

# 后端存储引擎
from sqlalchemy import create_engine
# 索引, 外键
from sqlalchemy import Index, ForeignKey
# 字段数据类型
from sqlalchemy import Integer, Numeric, String, DateTime, Boolean
# 元数据
from sqlalchemy import MetaData
# 约束
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint, ForeignKeyConstraint
# 表和列
from sqlalchemy import Table, Column

class DataAccessLayer():
    connection = None
    engine = None
    conn_string = None
    metadata = MetaData()

    def init(self, host = 'localhost', user = 'root', passwd = 'root', db = 'test', port = 3306):
        """初始化"""
        self.conn_string = "mysql+mysqldb://%s:%s@%s:%s/%s" % (user, passwd, host, port, db)
        self.engine = create_engine(self.conn_string, pool_recycle = 3600)
        print "创建Schema START"
        self.metadata.drop_all(self.engine)
        self.metadata.create_all(self.engine)
        print "创建Schema END"
        self.connection = self.engine.connect()

    ######################################################
    # Schema定义
    ######################################################
    ###################################################### 表COOKIES
    cookies = Table("COOKIES", metadata,
            Column("cookie_id", Integer(), primary_key = True),
            Column("cookie_name", String(50)),  # index = True
            Column("cookie_recipe_url", String(255)),
            Column("cookie_sku", String(55)),
            Column("quantity", Integer()),
            Column("unit_cost", Numeric(12, 2)),
            # 检查约束
            CheckConstraint("unit_cost >= 0.0", name = "unit_cost_positive"),
    #         # 索引
            Index("ix_cookies_cookie_name", "cookie_name"),
            Index("ix_cookie_sku_name", "cookie_sku", "cookie_name")
    )
    # Index("ix_cookies_cookie_name", cookies.c.cookie_name)  # 使用Table中字段
    # Index("ix_cookie_sku_name", cookies.c.cookie_sku, cookies.c.cookie_name)

    ###################################################### 表USERS
    users = Table("USERS", metadata,
            Column("user_id", Integer()),  # primary_key = True
            Column("username", String(15), nullable = False),  # unique = True
            Column("email_address", String(255), nullable = False),
            Column("phone", String(20), nullable = False),
            Column("password", String(25), nullable = False),
            Column("create_on", DateTime(), default = datetime.now),
            Column("update_on", DateTime(), default = datetime.now, onupdate = datetime.now),
            # 主键约束
            PrimaryKeyConstraint("user_id", name = "user_pk"),
            # 唯一性约束
            UniqueConstraint("username", name = "uix_username"),
     )


    ###################################################### 表ORDERS
    orders = Table("ORDERS", metadata,
            Column("order_id", Integer, primary_key = True),
            Column("user_id", ForeignKey("USERS.user_id")),  # 外键
            Column("shipped", Boolean(), default = False)
    )

    ###################################################### 表LINE_ITEMS
    line_items = Table("LINE_ITEMS", metadata,
            Column("line_items_id", Integer(), primary_key = True),
            Column("order_id"),  # ForeignKey("ORDERS.order_id")
            Column("cookie_id", ForeignKey("COOKIES.cookie_id")),  # 外键
            Column("quantity", Integer()),
            Column("extended_cost", Numeric(12, 2)),
            # 外键约束
            ForeignKeyConstraint(["order_id"], ["ORDERS.order_id"])
    )

    ###################################################### 表EMPLOYEE
    employee = Table("EMPLOYEE", metadata,
        Column("id", Integer(), primary_key = True),
        Column("manager", None, ForeignKey("EMPLOYEE.id")),
        Column("name", String(255), unique = True)
    )

dal = DataAccessLayer()

if __name__ == '__main__':
    dal.init()
