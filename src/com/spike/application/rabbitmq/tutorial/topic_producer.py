# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 18:39:33
topic生产者
@author: zhoujiagen
'''
import random
import sys

import pika


_facilities = ['anonymous', 'kern']
_severities = ['info', 'critical']

_exchange_name = 'topic_logs'  # exchange名称

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange = _exchange_name, exchange_type = 'topic')

# 路由键
_routing_key = random.choice(_facilities) + '.' + random.choice(_severities)
message = ' '.join(sys.argv[1:]) or 'hello, world!'
message = '[%15s] %s' % (_routing_key, message)
channel.basic_publish(
    exchange = _exchange_name,
    routing_key = _routing_key,
    body = message)

print 'send message(%s)' % message
connection.close()


