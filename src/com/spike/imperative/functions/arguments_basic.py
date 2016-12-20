# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 16:50:56
Python函数参数基础
不可变变量传值, 可变变量传引用
以tuple返回多个值
@author: zhoujiagen
'''

# 不可变变量传值
def f(a):
    print 'parameter: ', a
    a = 99
b = 88
f(b)
assert b == 88, 'b should be 88'

X = 1  # 不可变变量
a = X  # 共享变量
a = 2  # 仅修改a
assert X == 1, 'X should be 1'


# 可变变量传引用
def changer(a, b):
    print 'parameter: ', a, b
    a = 2
    b[0] = 'spam'
X = 1
Y = [1, 2]
changer(X, Y)
assert X == 1, 'X shoule be 1'
assert Y == ['spam', 2], 'Y should be [\'spam\', 2]'

L = [1, 2]  # 可变变量
L2 = L
L2[0] = 'spam'
assert L == ['spam', 2], 'L should be [\'spam\', 2]'

# 传拷贝, 以避免可变变量改变
X = 1
Y = [1, 2]
changer(X, Y[:])
assert Y == [1, 2], 'Y should be [1, 2]'


def multiple(x, y):
    x = 1
    y = [2, 3]
    return x, y  # 返回tuple

print multiple(None, None)
x , y = multiple(None, None)  # 多重赋值
print x, y
