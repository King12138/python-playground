# -*- coding: utf-8 -*-

'''
Created on 2016-12-13 11:54:05
文本文件处理
@author: zhoujiagen
'''

def write_text_file():
    """在当前目录下写入文本文件"""
    f = open('data.txt', 'w')  # 覆盖写模式

    f.write('hello\n')
    f.write('world\n')

    f.close()

def read_text_file():
    """读文本文件"""
    f = open('data.txt', 'r')  # 读模式
    text = f.read()  # 读入整个文件
    print text

    print text.split()  # 拆分

    # 使用迭代器
    for line in open('data.txt'): print line

if __name__ == '__main__':
    write_text_file()
    read_text_file()
