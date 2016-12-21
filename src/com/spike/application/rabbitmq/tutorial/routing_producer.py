# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 18:12:05
路由生产者, direct exchange:

info/warning/error to a consumer
error to another consumer
@author: zhoujiagen
'''

import random
import sys

import pika


_log_severity = ['info', 'warning', 'error']  # 日志级别

_exchange_name = 'direct_logs'  # exchange名称

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange = _exchange_name, exchange_type = 'direct')

_routing_key = random.choice(_log_severity)  # 路由键
message = ' '.join(sys.argv[1:]) or 'hello, world!'
message = '[%7s] %s' % (_routing_key, message)
channel.basic_publish(
    exchange = _exchange_name,
    routing_key = _routing_key,
    body = message)

print 'send message(%s)' % message
connection.close()
