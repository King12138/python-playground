# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 15:14:38
class_playground的单元测试
@author: zhoujiagen
'''

import unittest

from com.spike.objectoriented.class_playground import FirstClass, SecondClass, \
    ThirdClass

class FirstClassTest(unittest.TestCase):

    def runTest(self):
        x = FirstClass()
        y = FirstClass()
        print x, '\n', y

        x.setdata('King Arthur')  # 通过方法修改属性
        y.setdata(3.14159)

        x.display()
        y.display()

        x.data = 'New value'  # 直接访问属性
        x.display()

        x.anothername = 'spam'  # 直接添加实例属性
        assert hasattr(x, 'anothername'), 'x should have attribute `anothername`'
        assert  not hasattr(y, 'anothername')
        print x.anothername
        try:
            print y.anothername  # 访问不存在的实例属性
        except AttributeError as ae:
            print ae


class SecondClassTest(unittest.TestCase):
    def runTest(self):
        z = SecondClass()
        z.setdata(42)
        z.display()


class ThirdClassTest(unittest.TestCase):
    def runTest(self):
        a = ThirdClass('abc')
        a.display()
        print a

        b = a + 'xyz'  # 新的实例
        b.display()
        print b

        a.mul(3)  # 原位修改
        print a



# 最简单的类实现
class rec: pass

class SimplestClassTest(unittest.TestCase):

    def runTest(self):
        rec.name = 'Bob'  # 设置`类对象`的属性
        rec.age = 40
        print rec.name

        x = rec()  # 生成实例
        y = rec()
        print x.name, y.name

        x.name = 'Sue'  # 修改实例属性
        print rec.name, x.name, y.name

class OrdinaryObjectAttributesTest(unittest.TestCase):
        """输出对象(类, 实例)的属性"""
        rec.name = 'Bob'  # 设置`类对象`的属性
        rec.age = 40

        print rec.__dict__

        x = rec()
        x.name = 'Sue'
        print x.__dict__


        print x.__class__  # 实例所属的类
        print rec.__bases__  # 类的基类, 2.x中为()

class ClassAsRecordTest(unittest.TestCase):
    """类, 字典[,元组]的区别"""
    def runTest(self):
        _name = 'Bob'
        _age = 40.5
        _jobs = ['dev', 'mgr']

        # name, age, jobs
        tuple_based_record = (_name, _age, _jobs)
        print tuple_based_record
        print tuple_based_record[0]  #  访问元素

        dictionary_based_record = dict(name = _name, age = _age, jobs = _jobs)
        print dictionary_based_record
        print dictionary_based_record['name']  # 访问值

        # 基于类的记录
        rec.name = _name
        rec.age = _age
        rec.jobs = _jobs
        print rec.__dict__
        print rec.name  # 访问属性

        # 基于实例的记录
        record = rec()
        record.name = _name
        record.age = _age
        record.jobs = _jobs
        print record.__dict__
        print record.name  # 访问属性

        class Person():
            """常规类定义"""
            def __init__(self, name, jobs, age = None):
                self.name = name
                self.jobs = jobs
                self.age = age
            def info(self):
                return (self.name, self.jobs)

        regular_class_instance_based_record = Person(_name, _jobs, _age)
        print regular_class_instance_based_record.info()  # 访问属性

