# 1 数据结构

> TBD

# 2 命令式编程 - 控制结构, 异常处理, BIF等

> TBD

# 3 面向对象编程

> TBD

# 4 函数式编程支持

> TBD

# 5 工具 - 模块分发等
## 模块分发

+ Setuptools - See `dev-resources/setuptools-notes.md` and `setuptools-playground/README.md`
+ Distutils, Distutils2 - Well, they are not recommented.
+ Distribute - TBD

## virtualenv

See `dev-resources/virtualenv-notes.md` and `virtualenv-playground`.

> TBD

## 日志

> TBD

## 命令行解析Argparse

> TBD

# 6 OpenStack supported frameworks and tools

+ AMQP - RabbitMQ
+ SQLAlchemy
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
