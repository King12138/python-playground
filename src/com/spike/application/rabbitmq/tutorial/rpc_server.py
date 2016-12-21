# -*- coding: utf-8 -*-

'''
Created on 2016-12-21 19:11:58
RPC服务端
@author: zhoujiagen
'''
import pika

from com.spike.env.log import SpikeConsoleLogger

logger = SpikeConsoleLogger(logger_name = 'rpc').native()

_queue_name = 'rpc_queue'

def _fib(n):
    if n == 0: return 1
    elif n == 1: return 1
    else: return _fib(n - 1) + _fib(n - 2)

class FibonacciRpcServer():
    def start(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
        channel = connection.channel()
        channel.queue_declare(queue = _queue_name)

        channel.basic_qos(prefetch_count = 1)

        def on_request(channel, method, properties, body):
            logger.debug('incoming request: [\n\tchannel=%s \n\tmethod=%s \n\tproperties=%s \n\tbody=%s\n]'
                         % (channel, method, properties, body))
            n = int(body)
            response = _fib(n)

            # 接收到请求时称为生产者
            # 查找路由键, 同时返回相关性ID
            channel.basic_publish(
                exchange = '',
                routing_key = properties.reply_to,
                properties = pika.BasicProperties(correlation_id = properties.correlation_id),
                body = str(response)
            )
            channel.basic_ack(delivery_tag = method.delivery_tag)

        channel.basic_consume(on_request, queue = _queue_name)

        # 启动时是消费者
        print 'waiting for requests...'
        channel.start_consuming()

if __name__ == '__main__':
    server = FibonacciRpcServer()
    server.start()
