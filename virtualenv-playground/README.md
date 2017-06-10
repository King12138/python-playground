文档: https://virtualenv.pypa.io/en/stable/

使用pip安装. 使用参考: http://www.jianshu.com/p/08c657bd34f1

	$ virtualenv -h
	$ virtualenv --version
	15.1.0

	# 使用Python 2
	$ virtualenv -p `which python` scipy
	# 使用Python 3
	$ virtualenv -p `which python3` scipy3

	# 进入生成的目录后激活
	$ source ./bin/activate
	(scipy3) [/path/to/scipy3]$
	# 取消激活
	(scipy3) [/path/to/scipy3]$ deactivate

	# 查看当前依赖
	(scipy3) [/path/to/scipy3]$ bin/pip list --format=columns
	Package    Version
	---------- -------
	pip        9.0.1  
	setuptools 36.0.1
	wheel      0.29.0

	# 保存自定义依赖以便后续安装
	(scipy3) [/path/to/scipy3]$ bin/pip freeze
	(scipy3) [/path/to/scipy3]$ bin/pip freeze > requirement.txt
	(scipy3) [/path/to/scipy3]$ bin/pip install -r requirement.txt

	# 安装SciPy依赖
	(scipy3) [/path/to/scipy3]$ bin/pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
