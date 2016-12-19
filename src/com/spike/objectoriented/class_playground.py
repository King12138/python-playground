# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 15:11:13
简单的类定义, 用于展示基本语法
@author: zhoujiagen
'''

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print self.data


class SecondClass(FirstClass):
    # 覆盖父类中的方法
    def display(self):
        print 'Current value = %s' % (self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, otherValue):
        """返回新的实例"""
        return ThirdClass(self.data + otherValue)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, otherValue):
        """不返回新的实例, 原位修改"""
        self.data *= otherValue


