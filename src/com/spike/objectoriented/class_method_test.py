# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 19:27:54
方法的单元测试
@author: zhoujiagen
'''
import unittest

class NextClass:
    def printer(self, text):
        self.message = text
        print self.message

class MethodTest(unittest.TestCase):
    """instance.method(args...) 等价于 class.method(instance, args...)"""
    def runTest(self):
        x = NextClass()
        x.printer('instance call')
        print x.message

        NextClass.printer(x, 'class call')
        print x.message

class Super:
    def __init__(self, x):
        self.x = x

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)
        self.y = y

    def __repr__(self):
        return 'Sub: x=%s, y=%s' % (self.x, self.y)


class ConstructorTest(unittest.TestCase):
    """调用父类的构造器"""
    def runTest(self):
        I = Sub(1, 2)
        print I
