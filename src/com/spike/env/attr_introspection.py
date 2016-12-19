# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 17:12:23
类属性的自省工具
@author: zhoujiagen
'''

class AttrDisplay():
    """类属性的自省工具, 继承该类"""
    def gatherAttrs(self):
        """收集属性"""
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        """类的名称, 属性名称和值"""
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':
    """测试用例"""
    class RegularClass(AttrDisplay):
        count = 0  # 类属性(非实例属性)

        def __init__(self):
            self.attr1 = RegularClass.count
            self.attr2 = RegularClass.count + 1
            RegularClass.count += 2

    class RegularChildClass(RegularClass):
        pass

    print RegularClass.count
    print RegularChildClass.count

    X, Y = RegularClass(), RegularChildClass()
    print X
    print Y

    print RegularClass.count
    print RegularChildClass.count


    # ## BIF dir()
    print dir(X), '\n', dir(Y), '\n'
    # 输出自定义的属性
    print list(name for name in dir(X) if not name.startswith('__'))
