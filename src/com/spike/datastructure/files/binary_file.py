# -*- coding: utf-8 -*-

'''
Created on 2016-12-13 11:54:15
二进制字节文件: 使用struct模块
@author: zhoujiagen
'''

import struct

def write_binary_file():
    """
    写二进制字节文件
    REF PyDoc(http://localhost:7464/struct.html)
    """
    # big-endian, int, string(4位), short
    format_strings = '>i4sh'
    packed = struct.pack(format_strings, 77, b'spam', 8)
    print packed

    f = open('data.bin', 'wb')
    f.write(packed)
    f.close()

def read_binary_file():
    """读二进制字节文件"""
    f = open('data.bin', 'rb')

    data = f.read()
    print data
    print data[4:8]

    print list(data)  # 转换成列表

    # unpack, 重新组装成Python对象
    format_strings = '>i4sh'
    print struct.unpack(format_strings, data)

    f.close()

if __name__ == '__main__':
    write_binary_file()
    read_binary_file()
