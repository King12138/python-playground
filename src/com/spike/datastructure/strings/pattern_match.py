# -*- coding: utf-8 -*-

'''
Created on 2016-12-09 12:44:09
字符串模式匹配
@author: zhoujiagen
'''

import re

if __name__ == '__main__':
    line = "Hello   Python world."
    pattern = 'Hello[ \t]*(.*)world'
    match = re.match(pattern, line)
    print match
    print match.groups()
    print match.group(0)  # group 0 is all input
    print match.group(1)  # group 1 is the first '(''s content

    line2 = "/usr/home:lumberjack"
    pattern2 = '[/:](.*)[/:](.*)[/:](.*)'
    print ">", re.match(pattern2, line2).groups()

    # 按模式split
    print re.split('[/:]', line2)
