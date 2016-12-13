# -*- coding: utf-8 -*-

'''
Created on 2016-12-13 17:49:30
函数示例
@author: zhoujiagen
'''

def welcome():
    print 'hello, there.'

# 参数检测
def power(param):
    """广义的二次幂"""
    if isinstance(param, type(1)):  # 整数
        return param ** 2
    elif isinstance(param, set):  # 集合
        return param
    else:
        return param * 2

# TODO: 添加使用参数匹配语法的示例

# 是否支持嵌套函数(是)
def outer():
    print 'outer'

    def inner():
        # outer() # NEVER DO THIS
        print 'inner'

    inner()

if __name__ == '__main__':
    # welcome()

#     print power(2)
#     print power('2')
#     print power([2])
#     print power((2,))
#     print power({2})

    try:
        outer()
    except RuntimeError as e:
        print 'error: ', e

