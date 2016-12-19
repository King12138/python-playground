# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 16:12:34
具体的类层次示例
@author: zhoujiagen
'''

class Person():
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return 'Person[name=%s, job=%s, pay=%d]' % (self.name, self.job, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    # 子类中自定义行为
    def giveRaise(self, percent, bonus = .10):
        # self.pay = int(self.pay * (1 + percent + bonus))
        # 使用类方法
        Person.giveRaise(self, percent + bonus)

    def somethingElse(self):
        print 'Well, do something else...'


# 通过聚合而不是继承使用类
class ManagerV2():
    def __init__(self, name, pay):
        # 嵌入Person对象(object embedding)
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus = .10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        """获取属性"""
        return getattr(self.person , attr)  # 委托给person对象

class Department():
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print person
