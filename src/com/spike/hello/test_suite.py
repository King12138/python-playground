# -*- coding: utf-8 -*-  

'''
Created on 2016-12-07 11:57:48
将测试用例聚合成测试套件
@author: zhoujiagen
'''
import unittest

from com.spike.hello.multiple_test import WidgetTestCase


class WidgetTestSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self, map(WidgetTestCase, "testDefaultSize", "testResize"))
