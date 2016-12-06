# -*- coding: utf-8 -*-

'''
Created on 2016-12-06 12:41:22
测试fixture
@author: zhoujiagen
'''

import unittest

from com.spike.hello.domain import Widget


class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")

class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        assert self.widget.size() == (50, 50), 'incorrect default size'

class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100, 150)
        assert self.widget.size() == (100, 150), 'wrong size after resize'
