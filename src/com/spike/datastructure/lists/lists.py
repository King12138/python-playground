# -*- coding: utf-8 -*-

'''
Created on 2016-12-12 12:19:13
列表
@author: zhoujiagen
'''

def sequence_operation():
    """sequence操作"""
    L = [123, 'Spam', 1.23]  # 三个不同类型对象的列表
    print L
    print len(L)  # 获取列表的长度

    # 索引, 切片, 串接
    print L[0]
    print L[:3]
    print L + [4, 5, 6]  # 非原位修改
    print L * 2  # 非原位修改
    print L

    # 修改元素
    L[1] = 'SPAM'
    print L

def type_specific_operation():
    """列表类型上的操作"""
    L = [123, 'Spam', 1.23]
    print L
    L.append('NI')  # 从列表尾部追加, 原位修改
    print L

    L.pop(2)  # 删除元素, 原位修改
    print L
    del L[2]  # 删除元素, 原位修改
    print L

    M = ['bb', 'aa', 'cc']
    print M
    M.sort()  # 排序, 原位修改
    print M
    M.reverse()  # 逆序, 原位修改
    print M


def bounds_checking():
    """边界检查"""
    L = [123, 'Spam', 1.23]
    print L

    # 通过索引访问
    try:
        L[99]
    except IndexError as ie:
        print ie

    # 通过索引赋值
    try:
        L[99] = 1
    except IndexError as ie:
            print ie

def nesting():
    """嵌套列表: 矩阵等"""
    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print M

    # 访问元素
    print M[1]
    print M[1][2]

    # 赋值
    M[1] = [44, 55]  # 仅是矩阵的模拟, 各行元素长度可以不一致
    print M

def comprehension():
    """列表推导(生成列表)"""
    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print M

    # 获取第2列中元素构成的列表
    col2 = [row[1] for row in M]
    print col2
    # print M

    print [row[1] + 1 for row in M]
    print [row[1] for row in M if row[1] % 2 == 0]  # 过滤

    # 获取对角元素构成的列表
    diag = [M[i][i] for i in [0, 1, 2]]
    print diag

    # 字符串列表
    print [c * 2 for c in 'Spam']

    # range
    # Python 3.x中需要使用list()
    print list(range(4))  # [0, 4)
    print list(range(-6, 7, 2))  # 带step 2

    # 生成列表的列表, 即多个值
    print [[x ** 2, x ** 3] for x in range(4)]
    print [[x, x / 2 , x * 2] for x in range(-6, 7, 2) if x > 0]

def comprehension_generator():
    """生成器(generator)"""
    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    G = (sum(row) for row in M)  # 使用()
    print G
    print next(G)
    print next(G)
    print next(G)

    try:
        print next(G)
    except StopIteration as si:
        print 'Stop iteration', si

    # 或者使用内建的map
    print list(map(sum, M))

def comprehension_set():
    """使用推导生成集合"""
    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print {sum(row) for row in M}  # 使用{}

def comprehension_dictionary():
    """使用推导生成字典"""
    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print {i : sum(M[i]) for i in range(3)}  # 使用{key: value}


if __name__ == '__main__':
    # sequence_operation()
    # type_specific_operation()
    # bounds_checking()
    # nesting()

    # comprehension()
    # comprehension_generator()
    # comprehension_set()
    comprehension_dictionary()
