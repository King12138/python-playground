# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 19:36:17
类继承的单元测试
集成/替换(覆盖)/扩展/提供者
@author: zhoujiagen
'''
import unittest

class Super:
    def method(self):
        print 'in Super.method'  # 默认行为

    def delegate(self):
        self.action()  # 期望action()被定义

    def action(self):
        # 实现抽象基类
        # assert False, 'action must be defined!' # raise AssertionError
        raise NotImplementedError('action must be defined!')


class Inheritor(Super):
    pass  # 直接继承方法

class Replacer(Super):
    def method(self):  # 完全替换方法
        print 'in Replacer.method'

class Extender(Super):
    def method(self):  # 扩展方法
        print 'starting Extender.method'
        Super.method(self)
        print 'ending Extender.method'

class Provider(Super):
    def action(self):  # 提供(父类中使用的)需要的方法
        print 'in Provider.action'


class ClassInheritanceTest(unittest.TestCase):
    def runTest(self):
        for klass in (Inheritor, Replacer, Extender):
            print '\n===', klass.__name__
            klass().method()

        print '\n=== Provider'
        x = Provider()
        x.delegate()


        # 模拟实现抽象基类
        sub = Inheritor()
        try:
            sub.delegate()
        except NotImplementedError as nie:
            print 'NotImplementedError found: ', nie

