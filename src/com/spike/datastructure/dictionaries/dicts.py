# -*- coding: utf-8 -*-

'''
Created on 2016-12-12 13:10:04
字典
@author: zhoujiagen
'''

def dict_creation():
    """字典的创建"""
    # 方式1
    D = {'food': 'Spam', 'quantity' : 4, 'color': 'pink'}
    print D

    # 方式2
    D = {}
    D['food'] = 'Spam2'
    D['quantity'] = 5
    D['color'] = 'pink2'
    print D

    # 方式3: 使用dict关键字
    D = dict(food = 'Spam3', quantity = 6, color = 'pink3')
    print D
    # 使用zip BIF
    D = dict(zip(['food', 'quantity', 'color'], ['Spam4', 7, 'pink4']))
    print D

def nesting():
    """嵌套结构和元素访问"""
    record = {'name': {'first': 'Bob', 'last' : 'Smith'},
              'jobs': ['dev', 'mgr'],
              'age': 40.5
              }
    print record

    # 元素访问
    print record['name']
    print record['name']['last']

    print record['jobs']
    record['jobs'].append('test')
    print record['jobs']

    print record

    # 清空字典
    record.clear()
    print record
    # 删除字典对象的空间
    record = 0
    print record

def dict_key_exists():
    """检查字典中键的存在性"""
    D = {'a' : 1, 'b':2, 'c':3}
    print D

    try:
        D['d']
    except KeyError as ke:
        print 'wrong key', ke

    # 检查键的存在性
    print 'd' in D
    if not 'd' in D:
        print 'missing key'

    D['d'] = 4
    print D
    print 'd' in D

    # 键不存在时执行默认值
    print D.get('f', None)
    print D['f'] if 'f' in D else None

def dict_keys():
    """字典键的操作: 排序"""
    D = {'a' : 1, 'b':2, 'c':3}
    print D

    # 获取字典的键
    Ks = list(D.keys())
    print Ks
    Ks.sort()  # 原位列表排序

    # for循环
    for key in Ks:
        print key, '=>' , D[key]

    # sorted(dictionary)返回排序的列表
    for key in sorted(D):
        print key, '=>' , D[key]
    print D

    for c in 'Spam':
        print c

    # while循环
    n = 4
    while n > 0:
        print 'spam' * n
        n -= 1

def iteration():
    """迭代"""
    squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
    print squares

    # 等价的for循环
    # 列表推导/函数式BIF(map, filter)一般比for循环快
    squares = []
    for x in [1, 2, 3, 4, 5]:
        squares.append(x ** 2)
    print squares


if __name__ == '__main__':
    # dict_creation()
    # nesting()
    # dict_key_exists()
    # dict_keys()
    iteration()
