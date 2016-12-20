# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 15:51:29
显示实例的类层次树
@author: zhoujiagen
'''

DEFAULT_INDENT = 3
DEFAULT_INDENT_SYMBOL = '='

def instance_tree(instance):
    print '\ntree of instance[%s]' % instance
    class_tree(instance.__class__, DEFAULT_INDENT, set())

def class_tree(klass, indent, viewedKlassSet):
    """
    显示类的层次, 去除冗余
    """
    if klass.__name__ in viewedKlassSet: return
    else:
        print DEFAULT_INDENT_SYMBOL * indent + klass.__name__
        viewedKlassSet.add(klass.__name__)

    for superKlass in klass.__bases__:
        class_tree(superKlass, indent + DEFAULT_INDENT, viewedKlassSet)


if __name__ == '__main__':
    """用例"""
    class A : pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass

    instance_tree(A())
    instance_tree(B())
    instance_tree(C())
    instance_tree(D())
    instance_tree(E())
    instance_tree(F())

