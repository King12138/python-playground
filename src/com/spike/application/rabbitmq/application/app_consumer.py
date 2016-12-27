# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 19:49:09
app消费者
@author: zhoujiagen
'''

from com.spike.application.rabbitmq.application.app_conn_mgmt import ApplicaitonMQConnection, \
    default_consumer_callback

connection = ApplicaitonMQConnection().getConnection()

channel = connection.channel()

channel.queue_declare(queue = 'hello')

channel.basic_consume(default_consumer_callback, queue = 'hello')

print 'waiting for messages...'
channel.start_consuming()


