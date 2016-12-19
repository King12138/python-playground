# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 16:13:02
具体的类层次示例的单元测试
@author: zhoujiagen
'''

import unittest

from com.spike.objectoriented.classes_example import Person, Manager, ManagerV2, \
    Department


class PersonTest(unittest.TestCase):
    def runTest(self):
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job = 'dev', pay = 100000)
        print bob
        print sue

        assert 'Smith' == bob.lastName(), 'should be `Smith`'

        bob.pay = 100
        bob.giveRaise(.1)
        assert 110 == bob.pay, 'should be 110'

class ManagerTest(unittest.TestCase):
    def runTest(self):
        tom = Manager('Tom Jones', pay = 10000)
        print tom

        tom.giveRaise(.1)
        assert 12000 == tom.pay, 'should be 12000'

        tom.somethingElse()

class ManagerV2Test(unittest.TestCase):
    """聚合而不是继承类"""
    def runTest(self):
        tom = ManagerV2('Tom Jones', pay = 10000)
        print tom

        print tom.name  # 访问属性

        tom.giveRaise(.1)  # 调用方法
        assert 12000 == tom.pay, 'should be 12000'


class PolymorphismTest(unittest.TestCase):
    """多态测试"""
    def runTest(self):
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job = 'dev', pay = 100000)
        tom = Manager('Tom Jones', pay = 10000)

        for obj in (bob, sue, tom):
            obj.giveRaise(.1)
            print obj

class DepartmentTest(unittest.TestCase):
    def runTest(self):
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job = 'dev', pay = 100000)
        tom = Manager('Tom Jones', pay = 10000)

        department = Department(bob, sue)
        department.addMember(tom)

        department.showAll()

        department.giveRaise(.1)
        department.showAll()

class IntrospectionToolsTest(unittest.TestCase):
    """自省工具: __class__, __dict__"""
    def runTest(self):
        bob = Person('Bob Smith')

        print bob.__class__  # 全限定名
        print bob.__class__.__name__  # 名称

        for key in bob.__dict__:
            print '%s => %s/%s' % (key, bob.__dict__[key], getattr(bob, key))


