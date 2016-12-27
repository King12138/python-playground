# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 17:29:36
发布订阅消费者
@author: zhoujiagen
'''
import pika

_exchange_name = 'logs'  # exchange名称

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange = _exchange_name, exchange_type = 'fanout')

result = channel.queue_declare(exclusive = True)  # 只允许当前连接访问
queue_name = result.method.queue  # 获取生成的队列名称
# 将队列绑定到exchange
channel.queue_bind(queue = queue_name, exchange = _exchange_name)

def consumer_callback(channel, method, properties, body):
    """
                channel: BlockingChannel
                method: spec.Basic.Deliver
                properties: spec.BasicProperties
                body: str or unicode
    """
    print 'receive message(%s)' % body

channel.basic_consume(consumer_callback, queue = queue_name, no_ack = True)

print 'start receiving message...'
channel.start_consuming()
