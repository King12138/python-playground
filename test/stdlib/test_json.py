# -*- coding: utf-8 -*-

'''
Created on 2017-10-12 16:57:18
json
@author: zhoujiagen
'''

import json

if __name__ == '__main__':
    import sys
    print json.dumps(sys.path, indent = 4)
