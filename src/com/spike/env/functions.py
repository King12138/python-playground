# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 17:45:15
函数的工具类
@author: zhoujiagen
'''
import math

from com.spike.env.log import SpikeConsoleLogger


logger = SpikeConsoleLogger("functions").native()

def tracer(func, *args, **kwargs):
    """函数func添加调用日志输出"""
    logger.debug("calling %s(%s, %s)" % (func.__name__, args, kwargs))
    # return func(*args, **kwargs)
    return apply(func, args, kwargs)  # 使用BIF apply()


if __name__ == '__main__':
    """用例"""
    print tracer(math.pow, *(2, 100))
