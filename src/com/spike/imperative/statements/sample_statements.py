# -*- coding: utf-8 -*-

'''
Created on 2016-12-14 12:08:09
示例语句, 见Learning Python 5th Edition P.320
@author: zhoujiagen
'''

from com.spike.env.log import SpikeConsoleLogger
console_logger = SpikeConsoleLogger().native()

def _assignment():
    """赋值"""
    a, b = 'good', 'bad'
    print a, b

def _call():
    """函数/方法调用"""
    console_logger.debug("hello")

def _print():
    """打印输出"""
    print "hello", " python"

def _if_elif_else():
    """if/elif/else分支"""
    text = 'hello, python'
    if 'erlang' in text:
        print 'erlang found'
    elif 'python' in text:
        print 'python found'
    else:
        print 'nothing found'

def _for_else():
    """for循环和else"""
    for c in 'hello, python':
        if c == 'a':
            print 'found a'
            break
    else:
        print 'not found a'

def _while_else():
    """while循环和else"""
    text = 'hello, python'
    n = len(text)
    while n > 0:
        if(text[n - 1] == 'a'):
            print 'found a'
            break
        n -= 1
    else:
        print 'not found a'

def _pass():
    """pass, 语句占位符"""
    pass

def _break():
    """break语句"""
    for c in 'hello, python':
        if c == 'p':
            print 'found p, break!'
            break

def _continue():
    """continue语句"""
    for c in 'hello, python':
        if c != 'p':
            print 'found %c not p, continue!' % (c)

def _def():
    """函数和方法定义"""

    def nested_function():
        """嵌套函数定义"""
        print 'hello, python'

    nested_function()  # 调用

def _return():
    """return语句"""
    def nested_function():
        """嵌套函数定义"""
        return 'hello, python'

    text = nested_function()
    print 'returned %s' % (text)

def _yield():
    """生成器函数"""

    def generator_function(num):
        for i in range(num):
            yield i * 2

    G = generator_function(5)

    # 遍历生成器
    for i in G:
        print i

x_outer = 'module-level'
def _global():
    """global语句"""

    x_outer = 'function-level'
    def nested_function():
        global x_outer, y_outer
        x_outer = 'nested-function-level'
        y_outer = 'y'
        console_logger.info(x_outer)

    nested_function()  # call

    console_logger.info(x_outer)
    try:
        console_logger.info(y_outer)
    except NameError as ne:
        print 'cannot found y_outer: ', ne

X = 99
def changeX():
    global X
    X = 100

def _nonlocal_3x():
    """skip!!!"""
    pass

def _import():
    """导入模块"""
    import random
    print random.Random().random()

def _from():
    """导入模块中属性"""
    from random import Random
    print Random().random()

def _class():
    """类定义"""
    pass

def _try_except_finally():
    """异常捕获"""
    try:
        1 / 0
    except ZeroDivisionError as ne:
        print '/0 error: ', ne
    finally:
        print 'now world is quiet'

def _raise():
    """抛出异常"""
    try:
        raise Exception("error")
    except Exception as e:
        print 'caught exception: ', e

def _assert():
    """BIF断言"""
    X = 5; Y = 6

    try:
        assert X > Y, 'X is too small'
    except AssertionError as ae:
        print 'caught assertion error: ', ae

def _with_as():
    """自动释放资源, 2.6+, 3.x"""
    with open('data.txt') as myfile:
        content = ''
        for line in myfile:
            content += line + '\n'
        print content

        # myfile.close()

def _del():
    """删除引用: """
    # 1 data[i], data[i:j]
    data = [1, 2, 3, 4, 5]
    print data
    del data[0]
    print data
    del data[1:2]
    print data

    # 2 obj.attr
    class C():
        def __init__(self, name):
            self.name = name

    c = C("C")
    print c.name
    del c.name
    try:
        print c.name
    except AttributeError as ae:
        print 'found attribute error: ', ae

    # 3 variable
    variable = 1
    print variable
    del variable
    try:
        print variable
    except UnboundLocalError as ule:
        # 变量在赋值之前被引用
        print 'found unbound variable error: ' , ule


if __name__ == '__main__':
    # _assignment()
    # _call()
    # _print()
    # _if_elif_else()
    # _for_else()
    # _while_else()
    # _pass()
    # _break()
    # _continue()
    # _def()
    # _return()
    # _yield()

    # global, 相对于模块级别
#     _global()
#     console_logger.info(x_outer)
#
#     console_logger.info(X)
#     changeX()
#     console_logger.info(X)

    # _import()
    # _from()

    # _try_except_finally()
    # _raise()

    # _assert()

    # _with_as()

    _del()
