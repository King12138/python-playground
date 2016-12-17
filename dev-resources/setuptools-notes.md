Setuptools工具使用记录

# 1 资源

+ [Wikipedia - Setuptools](https://en.wikipedia.org/wiki/Setuptools)
+ [Python Package Index(PyPi) - setuptools](https://pypi.python.org/pypi/setuptools)
+ [IBM developerWorks -可爱的 Python: 使用 setuptools 孵化 Python egg](http://www.ibm.com/developerworks/cn/linux/l-cppeak3.html
): 有setuptools的起源和使用介绍; egg的介绍.
+ [Python包管理工具setuptools详解](http://yansu.org/2013/06/07/learn-python-setuptools-in-detail.html): 可作为快速入门用.

## 文档

+ [Setuptools文档 - Home](https://setuptools.readthedocs.io/en/latest/)
+ [Setuptools文档 - Easy Install](https://setuptools.readthedocs.io/en/latest/easy_install.html)

> Easy Install is a python module (easy_install) bundled with setuptools that lets you automatically download, build, install, and manage Python packages.

+ [Setuptools文档 - 使用pkg_resources做包发现和资源访问](https://setuptools.readthedocs.io/en/latest/pkg_resources.html)
+ [Setuptools文档 - Python Egg的内部结构](https://setuptools.readthedocs.io/en/latest/formats.html)

## 相关资源

+ [distutils](https://docs.python.org/2/library/distutils.html)

> The distutils package provides support for building and installing additional modules into a Python installation.
> 
> In particular, setuptools is an enhanced alternative to distutils.
> 
> The recommended pip installer runs all setup.py scripts with setuptools, even if the script itself only imports distutils.

+ [distutils2](https://pypi.python.org/pypi/Distutils2)

> Distutils2 development is stopped.  
> tl;dr: keep using setuptools and pip for now, don’t use distutils2.

+ [pip](https://pip.pypa.io/en/stable/)
+ [Python包(PyPA)安装和打包推荐工具](https://packaging.python.org/current/)

+ [PyPi - stevedore](https://pypi.python.org/pypi/stevedore)
+ [OpenStack - stevedore](http://git.openstack.org/cgit/openstack/stevedore/)


# 2 安装

## 2.1 推荐的启动方式

下载[ez_setup.py](https://bootstrap.pypa.io/ez_setup.py), 在目标Python环境中执行.

## 2.2 UNIX中安装

	wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
	
	# Mac - NOT WORKING
	wget https://bootstrap.pypa.io/ez_setup.py
	sudo python ez_setup.py install
	## 哎...
	sudo pip install --upgrade pip setuptools
	## then
	source .bash_profile

# 3 把玩

见setuptools-playground/README.md.


# 4 包发现和资源访问: pkg_resources模块

> The pkg_resources module distributed with setuptools provides an API for Python libraries to access their resource files, and for extensible applications and frameworks to automatically discover plugins.

术语的解释: [[Distutils] Terminology for distributions, eggs, setuptools, etc.](https://mail.python.org/pipermail/distutils-sig/2005-June/004652.html)

