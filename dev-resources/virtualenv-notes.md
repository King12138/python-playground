Virtualenv工具使用记录

> virtualenv is a tool to create isolated Python environments.


# 1 资源

+ [Python--Virtualenv简明教程](http://www.jianshu.com/p/08c657bd34f1): 可作为快速入门教程
+ [Virtualenv - 中文文档](http://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html)
+ [Virtualenv - 英文文档](https://virtualenv.pypa.io/en/stable/)

# 2 安装

	[~]$ python --version
	Python 2.7.10
	[~]$ pip --version
	pip 9.0.1 from /Library/Python/2.7/site-packages (python 2.7)
	[~]$ which virtualenv
	
	[~]$ sudo pip install virtualenv
	[~]$ which virtualenv
	/usr/local/bin/virtualenv
	[~]$ virtualenv --version
	15.1.0
	
# 3 辅助工具: [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/index.html)

> 提供了一系列命令使得和虚拟环境工作变得愉快许多。它把你所有的虚拟环境都放在一个地方。

