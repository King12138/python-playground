# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 18:51:18
应用的随机模块
@author: zhoujiagen
'''
from random import Random


def next_bool():
    """返回随机的布尔值"""
    _random_int = int(Random().random() * 10 % 2)
    _bool = _random_int == 0
    return _bool

def random_element(seq):
    """返回序列中的随机元素"""
    import random
    return random.choice(seq)
