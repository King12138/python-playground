# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 14:53:22
命名空间(Namespace)
@author: zhoujiagen
'''
from com.spike.env.log import SpikeConsoleLogger

logger = SpikeConsoleLogger(logger_name = "namespace").native()

X = 11  # 全局(模块)变量

def f():
    logger.info(X)  # 访问全局变量

def g():
    X = 22  # 函数内部变量, 遮盖全局变量
    logger.info(X)

class C:
    X = 33  # 类属性
    def m(self):
        X = 43  # 方法内部变量
        X = X + 1
        self.X = 55  # 实例属性

if __name__ == '__main__':
    logger.info(X)
    f()
    g()

    obj = C()
    logger.info(obj.X)

    obj.m()
    logger.info(obj.X)
    logger.info(C.X)

    # 不能访问函数对象的内部属性
    try:
        logger.info(C.m.X)
    except AttributeError as ae:
        logger.error(ae)
    try:
        logger.info(g.X)
    except AttributeError as ae:
        logger.error(ae)
