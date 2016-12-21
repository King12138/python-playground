# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 16:53:46
工作队列生产者
@author: zhoujiagen
'''
import sys
import pika
from random import Random


_queue_name = 'task_queue'  # 队列名称

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

channel.queue_declare(queue = _queue_name, durable = True)  # 持久化的队列

message = ' '.join(sys.argv[1:]) or 'hello, world!'
message = '[%d] %s' % (Random().random() * 10, message)

print 'send message(%s)' % message
channel.basic_publish(
    exchange = '',
    routing_key = _queue_name,
    body = message,
    properties = pika.BasicProperties(delivery_mode = 2)  # 持久化消息
)

connection.close()

