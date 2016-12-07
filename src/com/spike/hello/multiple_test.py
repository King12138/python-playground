# -*- coding: utf-8 -*-  

'''
Created on 2016-12-07 11:52:22
包含多个测试方法的测试类
@author: zhoujiagen
'''

import unittest

from com.spike.hello.domain import Widget


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
    
    def testDefaultSize(self):
        assert self.widget.size() == (50, 50)
    
    def testResize(self):
        self.widget.resize(100, 150)
        assert self.widget.size() == (100, 150), "wrong size after resize"