# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
执行: benchmark.py n

向量加法: Python v.s. Numpy
向量1: 0~n-1 平方
向量2: 0~n-1 立方
'''
import sys
from datetime import datetime
import numpy as np


def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []

    for i in range(len(a)):
        a[i] = i ** 2 # 平方
        b[i] = i ** 3 # 立方
        c.append(a[i]+b[i])

    return c

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b

    return c


size = int(sys.argv[1]) # 命令行参数

start = datetime.now() # 计时
c = pythonsum(size)
end = datetime.now()
print "Last 2 elements of sum", c[-2:], ", Python spend ", (end - start).microseconds, " ms"

start = datetime.now()
c = numpysum(size)
end = datetime.now()
print "Last 2 elements of sum", c[-2:], ", Numpy spend ", (end - start).microseconds, " ms"
