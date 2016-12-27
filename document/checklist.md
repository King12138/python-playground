# 0 Pydoc

PyDoc的构成:
 
+ 描述部分
+ 模块(Modules)
+ 类(Classes)
+ 函数(Functions)
+ 数据(Data)

# 1 数据结构

见`com.spike.datastructure`.

# 2 命令式编程 - 控制结构, 异常处理, BIF等

基本语句示例见`com.spike.imperative.statements`.

内建模块中`__builtin__`见PyDoc `__builtin__.html`.

函数参数传递和解析见`com.spike.imperative.functions`.

# 3 面向对象编程

见`com.spike.objectoriented`.

# 4 函数式编程支持

> TBD

# 5 工具 - 模块分发等
## 模块分发

+ Setuptools - See `dev-resources/setuptools-notes.md` and `setuptools-playground/README.md`
+ Distutils, Distutils2 - Well, they are not recommented.
+ Distribute - TBD

## virtualenv

See `dev-resources/virtualenv-notes.md` and `virtualenv-playground`.

## 日志

Python内建的模块: `logging`, `logging.config`, `logging.handlers`, REF [The Python Standard Library](https://docs.python.org/2.7/library/index.html) section 15.7~15.9.

入门教程: [python logging模块使用教程](http://www.jianshu.com/p/feb86c06c4f4)

封装见`com.spike.env.log.py`.

## 命令行解析Argparse

> TBD

# 6 OpenStack supported frameworks and tools

+ AMQP - RabbitMQ

文档见`dev-resources/rabbitmq-notes.md`, `dev-resources/rabbitmq-python-notes.md`;
RabbitMQ官方提供的pika示例见`com.spike.application.rabbitmq.tutorial`

+ [SQLAlchemy](http://www.sqlalchemy.org/): The Python SQL Toolkit and Object Relational Mapper - 

文档见`dev-resources/SQLAlchemy-notes.md`;
MySQL数据库操作(MySQLdb和SQLAlchemy示例见`com.spike.application.database.mysql.tutorial`)

+ WSGI - 路由模块Routes, Paste, WebOb, Django
+ Eventlet(协程coroutine)

## OpenStack通用库Oslo

+ 命令行程序Cliff
+ 配置oslo.config
+ 数据库oslo.db
+ 国际化oslo.i18n
+ 消息化oslo.messaging
+ 使用插件stevedore
+ 控制任务执行[TaskFlow](https://wiki.openstack.org/wiki/TaskFlow)
+ 搭建OpenStack项目的cookiecutter
+ 策略抽象oslo.policy
+ root权限封装oslo.rootwrap
+ 单元测试oslo.test
+ 其他

> TBD

# 7 OpenStack core components

(1) Framework Design;  
(2) Source code entry;  
(3) Source code core abstractions and procedures.

+ 计算 - Nova
+ 存储 - Swift(object), Cinder(block), Glance(image)
+ 网络 - Neutron
+ 安全 - Keystone
+ 计量与监控 - Ceilometer
+ 控制面板 - Horizon
+ 部署 - TripleO

## 7.1 DevStack安装和配置

见`dev-resources/devstack-notes.md`.

> TBD
