# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 19:49:09
helloworld消费者
@author: zhoujiagen
'''

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'hello')


def consumer_callback(channel, method, properties, body):
    """         channel: BlockingChannel
                method: spec.Basic.Deliver
                properties: spec.BasicProperties
                body: str or unicode
    """
    print 'receive message(%s)' % body
channel.basic_consume(consumer_callback, queue = 'hello')

print 'waiting for messages...'
channel.start_consuming()


