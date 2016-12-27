# -*- coding: utf-8 -*-

'''
Created on 2016-12-20 19:48:57
app生产者
@author: zhoujiagen
'''

from com.spike.application.rabbitmq.application.app_conn_mgmt import ApplicaitonMQConnection


connection = ApplicaitonMQConnection().getConnection()
channel = connection.channel()

channel.queue_declare(queue = 'hello')

msg = 'Hello, world!'
print 'send message(%s)' % msg
channel.basic_publish(exchange = '', routing_key = 'hello', body = msg)

connection.close()
