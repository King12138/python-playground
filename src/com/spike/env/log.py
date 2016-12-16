# -*- coding: utf-8 -*-

'''
Created on 2016-12-16 12:23:01
日志, 使用logging模块

使用文件日志配置会在调用模块的当前目录下生成log.log文件
@author: zhoujiagen
'''

import logging
import sys

# 日志格式
fmt = "%(asctime)s %(threadName)s [%(levelname)-8s] %(filename)-20s %(lineno)-4d %(funcName)-10s - %(message)s"
# 日期格式
# datefmt = "%Y-%m-%d %H:%M:%S"
datefmt = "%H:%M:%S"

class SpikeLogger():
    """日志基类"""
    def debug(self, message):
        self.logger.debug(message)
    def info(self, message):
        self.logger.info(message)
    def warn(self, message):
        self.logger.warn(message)
    def error(self, message):
        self.logger.error(message)
    def critical(self, message):
        self.logger.critical(message)

    def native(self):
        """底层的logger"""
        return self.logger

class SpikeConsoleLogger(SpikeLogger):
    """控制台输出日志"""
    def __init__(self, logger_name = "DEBUG"):
        self.logger_name = logger_name

        # 1 logger
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 2 handler
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.DEBUG)
        # 3 formatter
        formatter = logging.Formatter(fmt, datefmt)

        # add handler and formatter to logger
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)

# 控制台输出底层logger
#console_logger = SpikeConsoleLogger().native()

class SpikeFileLogger(SpikeLogger):
    """文件输出日志"""
    def __init__(self, logger_name = "DEBUG", log_path = "./log.log"):
        self.log_path = log_path

        # 1 logger
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 2 handler
        fh = logging.FileHandler(self.log_path)
        fh.setLevel(logging.WARN)

        # 3 formatter
        # %(process)d, %(thread)d
        fmt = "%(asctime)s %(threadName)s [%(levelname)-8s] %(filename)-20s %(lineno)-4d %(funcName)-10s - %(message)s"
        # datefmt = "%Y-%m-%d %H:%M:%S"
        datefmt = "%H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)

        # add handler and formatter to logger
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)


if __name__ == '__main__':
    """使用案例"""
    logger = SpikeConsoleLogger().native()
    # print log info
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    
