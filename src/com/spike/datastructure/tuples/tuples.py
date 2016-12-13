# -*- coding: utf-8 -*-

'''
Created on 2016-12-13 11:43:42
元组
@author: zhoujiagen
'''

def creation():
    """创建"""
    T = (1, 2, 3)
    print T

    T2 = 'spam', 3.0, [11, 22, 33]
    print T2

def operation():
    """操作"""
    T = (1, 2, 3, 4)
    print T
    T2 = 'spam', 3.0, [11, 22, 33]
    print T2

    # 串接
    print T + (5, 6)
    print T

    # 索引和切片
    print T[0]
    print T[:-1]
    print T2[2][0]

def method():
    """方法"""
    T = (1, 2, 3, 4)
    print T

    print T.index(4)  # 元素4的索引
    print T.count(4)  # 元素4的数量

def immutable():
    """不可变性"""
    T = (1, 2, 3, 4)
    print T

    try:
        T[0] = 2
    except TypeError as te:
        print "tuple is immutable: ", te

    # 生成新元组
    T = (2,) + T[1:]
    print T

if __name__ == '__main__':
    # creation()
    # operation()
    # method()
    immutable()
