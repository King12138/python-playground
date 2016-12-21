# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 18:12:17
路由消费者
@author: zhoujiagen
'''
from random import Random
import pika

_exchange_name = 'direct_logs'  # exchange名称

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange = _exchange_name, exchange_type = 'direct')

result = channel.queue_declare(exclusive = True)  # 只允许当前连接访问
queue_name = result.method.queue  # 获取生成的队列名称


_log_severity = ['info', 'warning', 'error']  # 日志级别
_log_severities = []

_random_int = int(Random().random() * 10 % 2)
_bool = _random_int == 0
print _random_int, _bool
if _bool:
    _log_severities = _log_severity
else:
    _log_severities = ['error']


# 按路由键将队列绑定到exchange
print 'listen on %s' % _log_severities
for routingKey in  _log_severities:
    channel.queue_bind(
        queue = queue_name,
        exchange = _exchange_name,
        routing_key = routingKey
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
