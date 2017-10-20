# -*- coding: utf-8 -*-

'''
Created on 2017-10-20 10:12:05
使用SQLAlchemy Core的应用逻辑模块
@author: zhoujiagen
'''
from sqlalchemy import select

from sqlalchemy_core_db import dal

# IDE中报错, 但可执行
def get_orders_by_customer(cust_name, shipped = None, details = False):
        """按用户名称获取订单信息"""
        columns = [dal.orders.c.order_id, dal.users.c.username, dal.users.c.phone]
        joins = dal.users.join(dal.orders)

        if details:
            columns.extend([dal.cookies.c.cookie_name,
                                dal.line_items.c.quantity,
                                dal.line_items.c.extended_cost])
        joins = joins.join(dal.line_items).join(dal.cookies)

        cust_orders = select(columns)
        cust_orders = cust_orders.select_from(joins).where(dal.users.c.username == cust_name)

        if shipped is not None:
            cust_orders = cust_orders.where(dal.orders.c.shipped == shipped)

        return dal.connection.execute(cust_orders).fetchall()


if __name__ == '__main__':
    dal.init()

    print get_orders_by_customer('cookiemon', 1, True)
