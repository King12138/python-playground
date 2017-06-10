# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
ndarry的属性
'''
import numpy as np

a = np.arange(15).reshape(3,5)
print "a", a
print
print "a.shape", a.shape # 形状/维度元组: (3,5)
print
print "a.ndim", a.ndim # 维度数量: 2
print
print "a.dtype.name", a.dtype.name # 元素数据类型的名称: int64
print
print "a.itemsize", a.itemsize # 元素所占字节数: 8
print
print "a.size", a.size # 元素总数: 15
print
print "type(a)", type(a) # 数组的类型: numpy.ndarray
