# -*- coding: utf-8 -*-

'''
Created on 2016-12-09 12:02:13
字符串
@author: zhoujiagen
'''

def sequence_opeartions():
    """sequence操作"""
    S = 'Spam'  # 字符串定义
    print len(S)  # 字符串长度

    # pisitive index
    print S[0]
    # negative index
    print S[-1], S[-2]

    # slice
    print S[1:3]  # S[1], S[2]
    print S[1:]
    print S[:3]
    print S[:-1]
    print S[:]

    # 拼接
    print S + 'xyz'
    print S  # 不是原位修改
    print S * 8  # 重复

def immutability():
    """字符串的不可变性"""
    S = "Spam"
    try:
        S[0] = 'z'
    except TypeError as te:
        print "strings are immutable: ", te

    # 生成新对象
    S = 'z' + S[1:]
    print S

    # 转换为list
    L = list(S)
    print L
    L[1] = 'c'
    print L
    print ''.join(L)

    # 字节数组
    BA = bytearray(b'Spam')
    BA.extend(b'eggs')  # 串接
    print BA
    print BA.decode()  # 转换为字符串

def generic_sequence_methods():
    """通用的sequence方法"""
    S = "Spam"
    print S.find('pa')  # 查找
    print S.replace('pa', 'xyz')  # 替换, 生成新对象; 不是原位替换
    print S
    print S.upper()
    print S
    print S.isalpha()  # 数字/字母判断

    # split, strip
    line = 'aaa,bbb,ccc'
    print line.split(',')
    print line

    line2 = 'aaa,bbb,ccc\n'
    print line2.rstrip(), "."
    print line2, "."

def formatting_expression():
    """格式化字符串"""
    # 占位符
    print '%s, eggs, and %s' % ('spam', 'SPAM!')
    print '{0}, eggs, and {1}'.format('spam', 'SPAM!')
    print '{}, eggs, and {}'.format('spam', 'SPAM!')

    # 数值
    print '{:,.2f}'.format(296999.2567)  # ,分隔符
    print '%.2f | %+05d' % (3.14159, -23)  # 补全, 符号

def code_strings():
    """定义字符串的多种方式"""
    print 'A\nB\tC', '.'
    print ord('\n'), '.'

    # 跨行的字符串定义
    msg = """
aaa
    bbb'''cccc""ddd
eee
    """
    print msg, '.'

if __name__ == '__main__':
    # sequence_opeartions()
    # immutability()
    # generic_sequence_methods()
    # formatting_expression()
    code_strings()
