# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 17:26:17
参数收集和解包
@author: zhoujiagen
'''

# (1) 收集参数 - callee
def f(*args):
    # args是元组
    print args

f()
f(1)
f(1, 2)
f(1, 2, 3)

def g(**args):
    # args是字典
    print args
g()
try:
    g(1)
except TypeError as te:
    print te
g(a = 1, b = 2)  # 已关键字方式调用

def h(a, *args, **kwargs):
    print a, args, kwargs
h(1, 2, 3, x = 1, y = 2)


# (2) 解包参数 - caller
def func(a, b, c, d):
    print (a, b, c, d)

args = (1, 2)
args += (3, 4)
func(*args)  # 指示拆分元组, 按位置传入

kwargs = {'a':11, 'b':22, 'c':33}
kwargs['d'] = 44
func(**kwargs)  # 指示拆分字典, 按关键字传入

# 一些直接调用的变种
func(*(1, 2), **{'d':4, 'c':3})
func(1, *(2, 3), **{'d':4})
# func(*(1, 2), 3, 4) # SyntaxError: only named arguments may follow *expression
func(*(1, 2, 3), **{'d':4})
func(*(1, 2, 3), d = 4)

# func(1, *(2), c = 3, **{'d':4}) # TypeError: func() argument after * must be a sequence, not int
func(1, *(2,), c = 3, **{'d':4})


