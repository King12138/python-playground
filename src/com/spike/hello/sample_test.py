# -*- coding: utf-8 -*-

'''
Created on 2016-12-06 12:21:26
简单的单元测试
REF: [Python单元测试框架](http://pyunit.sourceforge.net/pyunit_cn.html)
@author: zhoujiagen
'''

import unittest

from com.spike.hello.domain import Widget


class SampleTest(unittest.TestCase):
    # 尝试将模块加入Python的导入检索路径
    # import sys
    # sys.path.append('/Users/jiedong/github_local/python-playground/test/com/spike/hello/domain')

    # 覆盖runTest方法
    def runTest(self):
        a = 1 + 1
        # 使用Python内置的assert
        assert a == 2, 'a should equal 2'
        widget = Widget("The widget")
        assert widget.size() == (50, 50), 'incorrect default size'
