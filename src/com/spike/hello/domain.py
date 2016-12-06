# -*- coding: utf-8 -*-

'''
Created on 2016-12-06 12:43:13
领域实体定义
@author: zhoujiagen
'''

class Widget():
    def __init__(self, name):
        self.name = name
        self.width, self.length = 50, 50
    def size(self):
        return (self.width, self.length)
    def resize(self, width, length):
        self.width, self.length = width, length
