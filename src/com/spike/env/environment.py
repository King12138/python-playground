# -*- coding: utf-8 -*-

'''
Created on 2016-12-13 15:59:40
查看Python环境
@author: zhoujiagen
'''

import sys
import json


if __name__ == '__main__':
    # 输出系统路径
    print json.dumps(sys.path, indent = 4)
