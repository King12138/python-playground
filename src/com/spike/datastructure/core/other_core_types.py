# -*- coding: utf-8 -*-

'''
Created on 2016-12-13 17:48:34
其他的核心类型: 布尔类型, 类型检查, None
@author: zhoujiagen
'''

def bool_type():
    "布尔类型"
    print True, False

    print True == 1, True == 2, True == -1
    print False == 0, False == 2, False == -1
    print True != False
    print 1 > 2, 1 < 2

def type_check():
    """类型检测"""
    L = [1, 2, 3]

    print type(L)
    print type(type(L))

    print type(L) == type([])
    print type(L) == list  # 使用type名称

    print isinstance(L, list)  # 实例检测
    print isinstance(L, type(L))
    print isinstance(L, type([]))

def None_type():
    """None类型"""
    print None
    L = [None] * 3
    print L


if __name__ == '__main__':
    # bool_type()
    # type_check()
    None_type()
