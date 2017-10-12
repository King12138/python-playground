# -*- coding: utf-8 -*-

'''
Created on 2017-10-12 17:00:26
inspect
https://docs.python.org/release/2.7.14/library/inspect.html

1 type and members
2 retrieve source code
3 class and function
4 interpreter stack

@author: zhoujiagen
'''

import inspect

class BaseClass(object):
    """Class BaseClass"""
    def __init__(self, arg1):
        self.arg1 = arg1

class DerivedClass(BaseClass):
    pass

class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

def f(a, b = 1, *pos, **named):
    pass


if __name__ == '__main__':

    a = BaseClass("A")

    # 1 type and members
    print "Member of a: ", inspect.getmembers(a)  # 获取对象的成员
    # 按路径获取模块信息
    print inspect.getmoduleinfo("/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/inspect.pyc")

    # 2 retrieve source code
    print
    print "Doc of a: ", inspect.getdoc(a)  # 获取对象的文档字符串
    print "Module of a: ", inspect.getmodule(a)  # 获取对象所属的模块
    print inspect.getmodule(inspect.getmodule)  # 获取方法所属的模块
    print "Source of BaseClass: ", inspect.getsource(BaseClass)  # 获取类的源码

    # 3 class and function
    print
    print inspect.getclasstree([DerivedClass, D])  # 类树
    print "ArgSpec of f: ", inspect.getargspec(f)  # 方法参数说明
    print inspect.getcallargs(f, 1, b = 2, c = 3, d = 4)  # 方法调用参数
    print "MRO of DerivedClass: ", inspect.getmro(DerivedClass)  # 方法解析顺序(mro)

    # 4 interpreter stack
    print
    current_stack = inspect.stack(context = 1)
    print "Current Stack: ", current_stack
    current_frame = inspect.currentframe()
    print "Current Frame: ", current_frame
    current_frame_traceback = inspect.getframeinfo(current_frame)
    print "Current Frame's Traceback: ", current_frame_traceback
    del current_frame

