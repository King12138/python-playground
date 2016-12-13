# -*- coding: utf-8 -*-

'''
Created on 2016-12-13 17:52:53
集合
@author: zhoujiagen
'''

def creation():
    """创建"""
    S = set('spam')
    S2 = {'h', 'a', 'm'}
    print S, S2, (S, S2)

def operation():
    """操作"""
    S = set('spam')
    S2 = {'h', 'a', 'm'}

    print S & S2  # 交
    print S | S2  # 并
    print S - S2  # 差
    print S > S2  # 超集判断

def comprehension():
    """推导"""
    S = {x ** 2 for x in [1, 2, 3, 4, 5]}
    print S

def in_membership_test():
    """in成员关系判断"""
    print 'p' in set('spam'), 'p' in 'spam', 'ham' in ['egg', 'spam', 'ham']


if __name__ == '__main__':
    # creation()
    # operation()
    # comprehension()
    in_membership_test()
