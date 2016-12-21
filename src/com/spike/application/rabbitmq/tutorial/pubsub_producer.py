# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 17:29:28
发布订阅生产者, fanout exchange
all message to multiple consumers
@author: zhoujiagen
'''
import sys
import pika

_exchange_name = 'logs'  # exchange名称

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange = _exchange_name, exchange_type = 'fanout')

message = ' '.join(sys.argv[1:]) or 'hello, world!'
channel.basic_publish(exchange = _exchange_name, routing_key = '', body = message)

print 'send message(%s)' % message
connection.close()

