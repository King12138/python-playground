# -*- coding: utf-8 -*-

'''
Created on 2016-12-13 17:49:40
类示例
@author: zhoujiagen
'''

class Worker():
    """工作者类"""
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent = 0.1):
        self.pay *= (1.0 + percent)
    def __str__(self):
        return 'str: Worker(name=%s, pay=%d)' % (self.name, self.pay)
    def __repr__(self):
        return 'repr: Worker(name=%s, pay=%d)' % (self.name, self.pay)

if __name__ == '__main__':
    alice = Worker('Alice Smith', 5000)
    bob = Worker('Bob Junes', 6000)
    print alice, str(alice)
    print  bob, str(bob)

    print alice.lastName(), '; ', bob.lastName()

    print alice.pay
    alice.giveRaise()
    print alice.pay
    alice.giveRaise(0.2)
    print alice.pay
