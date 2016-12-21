# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 18:39:52
topic消费者

单个'#'接收所有消息
'*'可替换1个词
'#'可替换0或多个词
@author: zhoujiagen
'''
import pika

from com.spike.env.spike_random import random_element


_exchange_name = 'topic_logs'  # exchange名称

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange = _exchange_name, exchange_type = 'topic')

result = channel.queue_declare(exclusive = True)  # 只允许当前连接访问
queue_name = result.method.queue  # 获取生成的队列名称

_facilities = ['*', 'anonymous', 'kern']
_severities = ['*', 'info', 'critical']

_binding_keys = set()
for i in range(3):
    _binding_keys.add(random_element(_facilities) + "." + random_element(_severities))
print 'binding keys: %s' % _binding_keys
for binding_key in _binding_keys:
    channel.queue_bind(
        queue = queue_name,
        exchange = _exchange_name,
        routing_key = binding_key
    )

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
