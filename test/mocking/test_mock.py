# -*- coding: utf-8 -*-

'''
Created on 2017-10-20 13:44:37
Spike on module 'mock'
@author: zhoujiagen
'''

import unittest
import mock

class TestApplication(unittest.TestCase):

    @mock.patch("test_mock_app.app")
    def test_method(self, mock_app):
        _return_value = "hello, there"
        # mock返回值
        mock_app.method.return_value = _return_value
        # 调用
        result = mock_app.method()
        print result
        # 断言
        self.assertEqual(_return_value, result)
