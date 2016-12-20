# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 15:09:10
命名空间, 引入namespace模块
@author: zhoujiagen
'''
from com.spike.env.log import SpikeConsoleLogger

logger = SpikeConsoleLogger(logger_name = "namespace2").native()

import namespace

X = 66

if __name__ == '__main__':

    logger.info(X)
    logger.info(namespace.X)

    namespace.f()
    namespace.g()

    logger.info(namespace.C.X)
    I = namespace.C()
    logger.info(I.X)

    I.m()
    logger.info(I.X)
