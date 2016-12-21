# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 19:48:57
helloworld生产者
@author: zhoujiagen
'''

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'hello')

msg = 'Hello, world!'
print 'send message(%s)' % msg
channel.basic_publish(exchange = '', routing_key = 'hello', body = msg)

connection.close()
