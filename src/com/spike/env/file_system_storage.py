# -*- coding: utf-8 -*-

'''
Created on 2016-12-19 17:27:03
文件系统的存储
(1) pickle
Serializes arbitrary Python objects to and from a string of bytes
(2) dbm (named anydbm in Python 2.X)
Implements an access-by-key filesystem for storing strings
***(3) shelve
Uses the other two modules to store Python objects on a file by key
@author: zhoujiagen
'''
import shelve

from com.spike.env.log import SpikeConsoleLogger

logger = SpikeConsoleLogger().native()

class NotOpenedException(Exception):
    pass

class KeyValueFileSystemStorage():
    def __init__(self, filename = 'KeyValueFileSystemStorage_db'):
        self.filename = filename
        self.opened = False

    def put(self, key, value):
        logger.debug('put [key=%s, value=%s] to %s' % (key, value, self.filename))
        if not self.opened: raise NotOpenedException('should call open() firstly')

        self.db[key] = value

    def get(self, key):
        logger.debug('get [key=%s] from %s' % (key, self.filename))
        if not self.opened: raise NotOpenedException('should call open() firstly')

        try:
            return self.db[key]
        except KeyError:
            return None

    def open(self):
        self.db = shelve.open(self.filename)
        self.opened = True

    def flush(self):
        logger.debug('flush %s' % self.filename)
        if not self.opened: raise NotOpenedException('should call open() firstly')

        self.colse()
        self.open()

    def colse(self):
        logger.debug('close %s' % self.filename)
        self.db.close()
        self.opened = False

    def showAll(self):
        logger.debug('showAll %s' % self.filename)
        if not self.opened: raise NotOpenedException('should call open() firstly')

        print '=' * 100
        for key in self.db:
            print '%s => %s' % (key, self.db[key])
        print '=' * 100

if __name__ == '__main__':
    """原生的模块测试用例
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job = 'dev', pay = 100000)
        tom = Manager('Tom Jones', pay = 10000)
    
        # 存储
        filename = 'persondb'
        db = shelve.open(filename)
        for obj in (bob, sue, tom):
            db[obj.name] = obj
        db.close()
    
        # 读取
        db = shelve.open(filename)
        for key in db.keys():
            print db[key]
        for key in db:
            print '%s => %s' % (key, db[key])
    
        # 更新
        _bob = db['Bob Smith']
        _bob.pay = 50000
        _bob.giveRaise(.1)
        db['Bob Smith'] = _bob
        db.close()
    
        # 读取最终结果
        db = shelve.open(filename)
        for key in db:
            print '%s => %s' % (key, db[key])
        db.close()
    """
    from com.spike.objectoriented.classes_example import Person, Manager
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    tom = Manager('Tom Jones', pay = 10000)

    # init
    storage = KeyValueFileSystemStorage('persondb')

    # open
    storage.open()

    storage.showAll()


    # put
    for obj in (bob, sue, tom):
        storage.put(obj.name, obj)

    # flush
    storage.flush()
    storage.showAll()

    _bob = storage.get('Bob Smith')
    _bob.pay = 5000
    _bob.pay = 50000
    _bob.giveRaise(.1)
    storage.put('Bob Smith', _bob)
    storage.flush()
    storage.showAll()

    # close
    storage.colse()
