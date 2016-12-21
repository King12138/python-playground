# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 16:53:56
工作队列消费者
competing consumers
@author: zhoujiagen
'''
import time
import pika

_queue_name = 'task_queue'  # 队列名称

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

channel.queue_declare(queue = _queue_name, durable = True)  # 持久化的队列

channel.basic_qos(prefetch_count = 1)  # 预取数量为1
def consumer_callback(channel, method, properties, body):
    """
                channel: BlockingChannel
                method: spec.Basic.Deliver
                properties: spec.BasicProperties
                body: str or unicode
    """
    print 'receive message(%s)' % body
    time.sleep(1)  # 模拟消费者按数据执行的工作
    channel.basic_ack(delivery_tag = method.delivery_tag)  # ack

channel.basic_consume(consumer_callback, queue = _queue_name)

print 'start consuming...'
channel.start_consuming()
