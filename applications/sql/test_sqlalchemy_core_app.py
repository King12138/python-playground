# -*- coding: utf-8 -*-

'''
Created on 2017-10-20 17:18:28
sqlalchemy_core_app的单元测试
@author: zhoujiagen
'''


from decimal import Decimal
import unittest

import  mock

from sqlalchemy_core_db import dal
from sqlalchemy_core_app import get_orders_by_customer

class AppTest(unittest.TestCase):

    cookie_orders = [(u'wlk001', u'cookiemon', u'111-111-1111')]
    cookie_details = [
        (u'wlk001', u'cookiemon', u'111-111-1111',
         u'dark chocolate chip', 2, Decimal('1.00')),
        (u'wlk001', u'cookiemon', u'111-111-1111',
         u'oatmeal raisin', 12, Decimal('3.00'))
    ]

    @classmethod
    def setUpClass(cls):
        dal.init()
        from sqlalchemy_core_schema_and_data import  init_data
        init_data(dal.connection)

    def test_dummy(self):
        pass

    # 模块中对象
    @mock.patch("sqlalchemy_core_db.dal.connection")
    def test_orders_by_customer(self, mock_conn):
        # 模拟对象的调用链中的所有返回值
        mock_conn.execute.return_value.fetchall.return_value = self.cookie_orders
        result = get_orders_by_customer('')
        self.assertEqual(self.cookie_orders, result)

    # 注意装饰器应用顺序与方法参数顺序的对应关系
    @mock.patch("sqlalchemy_core_app.select")
    @mock.patch("sqlalchemy_core_db.dal.connection")
    def test_orders_by_customer_blank(self, mock_conn, mock_select):
        mock_select.return_value.select_from.return_value.where.return_value = []
        mock_conn.execute.return_value.fetchall.return_value = []
        result = get_orders_by_customer('')
        self.assertEqual([], result)
