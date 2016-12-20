# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 15:39:52
命名空间中嵌套的类
@author: zhoujiagen
'''
from com.spike.env.log import SpikeConsoleLogger

logger = SpikeConsoleLogger(logger_name = "namespace_nested_class").native()

X = 1

def nester():
    logger.info(X)

    class C:
        logger.info(X)  # 引用全局变量
        def method1(self):
            logger.info(X)  # 引用全局变量
        def method2(self):
            X = 3  # 方法局部变量, 遮盖全局变量
            logger.info(X)

    I = C()
    I.method1()
    I.method2()


def nester2():
    X = 2  # 方法局部变量, 遮盖全局变量
    logger.info(X)

    class C:
        logger.info(X)  # 引用nester2.X
        def method1(self):
            logger.info(X)  # 引用nester2.X
        def method2(self):
            X = 3  # 方法局部变量, 遮盖引用nester2.X
            logger.info(X)

    I = C()
    I.method1()
    I.method2()

def nester3():
    X = 2  # 方法局部变量, 遮盖全局变量
    logger.info(X)

    class C:
        X = 3  # 类属性, 遮盖nester3.X
        logger.info(X)  # 引用nester3.C.X
        def method1(self):
            logger.info(X)  # 引用nester3.C.X
            logger.info(self.X)  # 引用nester3.C.X
        def method2(self):
            X = 4  # 方法局部变量, 遮盖引用nester3.C.X
            logger.info(X)
            self.X = 5  # 实例属性, 遮盖nester3.C.X
            logger.info(self.X)

    I = C()
    I.method1()
    I.method2()

logger.info(X)  # 1
nester()  # 1/1/1/3
print '-' * 80
nester2()  # 2/2/2/3
print '-' * 80
nester3()  # 2/3/2/3/4/5
