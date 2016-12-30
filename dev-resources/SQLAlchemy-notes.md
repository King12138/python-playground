SQLAlchemy 概念和实践记录

# 0 资源

[SQLAlchemy download](http://www.sqlalchemy.org/download.html)
[SQLAlchemy 1.1 Documentation](http://docs.sqlalchemy.org/en/rel_1_1/)
[数据库方言](http://docs.sqlalchemy.org/en/rel_1_1/dialects/index.html)

# 1 安装和配置

	$ sudo pip install SQLAlchemy
	# 检查版本
	>>> import sqlalchemy
	>>> sqlalchemy.__version__
	'1.1.4'

# 2 使用(with code fragment)

创建连接 TBD
声明映射 TBD
创建schema TBD
创建session TBD
添加和更新对象 TBD
回滚 TBD

查询
`Query.filter()`中常用的过滤操作: `==`, `!=`, `like`, `in_`, `~...in_`, `== None`, `!= None`, `and_`, `or_`, `match`.
返回列表和标量 TBD
使用文本SQL TBD
统计 TBD  

构建关系