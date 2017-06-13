# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
数组的创建
'''

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# 从常规的Python元组和列表中创建
a = np.array((1,2,3))
b = np.array([1,2,3])
print "a", a, "\n"
print "b", b, "\n"

# 使用序列的序列
c = np.array([(1,2,3), (4,5,6)])
d = np.array([[1,2,3], [4,5,6]])
e = np.array([([1,2,3], [4,5,6])])
print "c", c, "\n", "d", d, "\n", "e", e, "\n"

# 创建时指定元素类型
f = np.array([[1,2], [3,4]], dtype=complex)
print "f", f, "\n"

# 使用routine
g = np.zeros((2,3))
h = np.ones((2,3,4), dtype=np.int16)
i = np.empty((2,3))
print "g", g, "\n", "h", h, "\n", "i", i, "\n"

# 数值序列
print np.arange(10, 30, 5), "\n"
print np.arange(0, 2, 0.3), "\n"

print np.linspace(0, 2, 9), "\n"
x = np.linspace(0, 2*pi, 100)
f = np.sin(x)
plt.plot(x, f)
plt.axis([0, 2*pi, -1, 1]) # [a,b,c,d]: axis1 range([a, b]), axis2 range: ([c, d])
plt.show()
