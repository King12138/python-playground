# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 19:20:52
类变量的单元测试
@author: zhoujiagen
'''
import unittest


class SharedData:
    spam = 42  # 类的属性

class SharedDataTest(unittest.TestCase):

    def runTest(self):
        # 实例继承了类的属性
        x = SharedData()
        y = SharedData()
        print SharedData.spam, x.spam, y.spam

        SharedData.spam = 99
        print SharedData.spam, x.spam, y.spam

        x.spam = 88  # 创建了实例属性
        print SharedData.spam, x.spam, y.spam

class MixedNames:
    # 类属性和实例属性同名
    data = 'spam'
    def __init__(self, value):
        self.data = value
    def display(self):
        print self.data, MixedNames.data

class MixedNamesTest(unittest.TestCase):
    def runTest(self):
        x = MixedNames(1)
        y = MixedNames(2)
        x.display()
        y.display()