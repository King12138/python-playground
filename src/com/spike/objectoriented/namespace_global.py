# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 15:22:24
命名空间, 关键字global
@author: zhoujiagen
'''
from com.spike.env.log import SpikeConsoleLogger
from com.spike.imperative.statements.sample_statements import _nonlocal_3x

logger = SpikeConsoleLogger(logger_name = "namespace_global").native()

X = 11

def g1():
    logger.info(X)

def g2():
    global X
    X = 22
    logger.info(X)

def h1():
    X = 33
    def nested():
        logger.info(X)
    nested()

# Python 3.X
# def h2():
#     X  = 33
#     def nested():
#         nonlocal X
#         X = 44


if __name__ == '__main__':
    logger.info(X)

    g1()
    g2()
    h1()
