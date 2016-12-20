# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 17:04:51
参数匹配模式
1 Positionals: matched from left to right
2 Keywords: matched by argument name
3 Defaults: specify values for optional arguments that aren’t passed
4 Varargs collecting: collect arbitrarily many positional or keyword arguments(callee)
5 Varargs unpacking: pass arbitrarily many positional or keyword arguments(caller)
6 Keyword-only arguments: arguments that must be passed by name(Python 3.x)

caller:
func(value)
func(name=value)
func(*iterable)
func(**dict)

callee:
def func(value)
def func(name=value)
def func(*name)
def func(**name)
def func(*other, name) - 3.x
def func(*, name=value) - 3.x


匹配参数的步骤:
1 位置参数
2 关键字参数
3 *name tuple - 命名约定 *args
4 **name dict - 命名约定 **kwargs
5 默认值参数

@author: zhoujiagen
'''

# (1) 关键字和默认参数
def f(a, b, c):
    print a, b, c
f(1, 2, 3)
f(c = 3, b = 2, a = 1)
f(1, c = 3, b = 2)
# 非关键字参数不能在关键字参数后面
# f(c = 3, 1, 2)  # SyntaxError: non-keyword arg after keyword arg
# f(c = 3, 2, a = 1) # SyntaxError: non-keyword arg after keyword arg

def g(a, b = 2, c = 3):
    print a, b, c
g(1)
g(1, 4)
g(1, 4, 5)
g(1, b = 22)  # 覆盖默认参数
# g(1, b = 22, 33) # SyntaxError: non-keyword arg after keyword arg

# 可变变量的默认值
def h(a = 1, b = []):
    b.append('spam')
    print a, b
# 多次调用间共享
h()  # 1 ['spam']
h()  # 1 ['spam', 'spam']

# def h2(a = 1, b): # SyntaxError: non-default argument follows default argument
def h2(a = 1, b = None):
    b = []  # 在函数内部初始化
    b.append('spam')
    print a, b
# 多次调用间不共享
h2()  # 1 ['spam']
h2()  # 1 ['spam']
