# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 19:12:06
RPC客户端
@author: zhoujiagen
'''
import uuid
import pika
from com.spike.env.log import SpikeConsoleLogger

logger = SpikeConsoleLogger(logger_name = 'rpc').native()

_queue_name = 'rpc_queue'

class FibonacciRpcClient():

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive = True)  # 只允许当前连接访问
        self.callback_queue_name = result.method.queue  # 获取生成的队列名称
        logger.debug('callback_queue_name=%s', self.callback_queue_name)

        # 变为消费者
        self.channel.basic_consume(
            self.on_response,
            queue = self.callback_queue_name,
            no_ack = True)

    def on_response(self, channel, method, properties, body):
        logger.debug('incoming response: [\n\tchannel=%s \n\tmethod=%s \n\tproperties=%s \n\tbody=%s\n]'
                     % (channel, method, properties, body))
        if self.corr_id == properties.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())  # 构造相关性ID

        # 调用时为生产者
        self.channel.basic_publish(
            exchange = '',
            routing_key = _queue_name,
            # 设置回复channel, 相关性ID
            properties = pika.BasicProperties(
                reply_to = self.callback_queue_name,
                correlation_id = self.corr_id),
            body = str(n))

        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)

if __name__ == '__main__':
    client = FibonacciRpcClient()
    print client.call(10)
