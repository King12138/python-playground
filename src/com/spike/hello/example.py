# -*- coding: utf-8 -*-

'''
Created on 2016-12-01 13:19:59
简单的模块(main)
@author: zhoujiagen
'''

import os


if __name__ == '__main__':
    import sys
    print sys.version
    env = os.environ
    for key, value in env.items():
        print key, "=", value
