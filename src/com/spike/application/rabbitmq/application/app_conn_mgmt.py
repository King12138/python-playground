# -*- coding: utf-8 -*-

'''
Created on 2016-12-22 17:37:01
应用连接管理
@author: zhoujiagen
'''
import pika
from pika.credentials import PlainCredentials
from com.spike.env.log import SpikeConsoleLogger


_host = 'localhost'
_port = 5672
_virtual_host = '/webcrawler'
_username = 'zhoujiagen'
_password = 'zhoujiagen'
_credentials = PlainCredentials(_username, _password)

_logger = SpikeConsoleLogger(logger_name = 'ApplicaitonMQConnection').native()

class ApplicaitonMQConnection():
    """应用的消息队列连接"""
    def __init__(self):
        _logger.debug('init mq connection...')
        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host = _host,
                    port = _port,
                    virtual_host = _virtual_host,
                    credentials = _credentials))
        self._init_flag = True

    def getConnection(self):
        return self.connection

    def close(self):
        self.connection.close()

def default_consumer_callback(channel, method, properties, body):
    """ 
        默认的消费回调
        :param channel: BlockingChannel
        :param method: spec.Basic.Deliver
        :param properties: spec.BasicProperties
        :param body: str or unicode
    """
    _logger.debug('incoming response: [\n\tchannel=%s \n\tmethod=%s \n\tproperties=%s \n\tbody=%s\n]'
                  % (channel, method, properties, body))
    _logger.info('receive message(%s)' % body)

if __name__ == '__main__':
    print not None
