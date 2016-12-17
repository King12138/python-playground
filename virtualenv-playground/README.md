使用virtualenv管理Python环境


# 1 创建环境

	# 查看帮助
	$ virtualenv -h

	$ virtualenv ENV
	New python executable in ..../python-playground/virtualenv-playground/ENV/bin/python
	Installing setuptools, pip, wheel...done.
	
	$ tree -L 1 ENV
	ENV
	├── bin
	├── include
	├── lib
	└── pip-selfcheck.json
	
# 2 使用

	# 激活
	$ source ENV/bin/activate
	# 停用
	(ENV) [..../virtualenv-playground]$ deactivate	
	
	
# 3 依赖管理

	(ENV) [..../virtualenv-playground]$ pip list
	pip (9.0.1)
	setuptools (32.1.0)
	wheel (0.29.0)
	
	(ENV) pip freeze
	(ENV) pip freeze > requirement.txt
	
	$ pip install -r requirement.txt 
	You must give at least one requirement to install (see "pip help install")

	### 安装依赖
	(ENV) pip install Trac
	
	(ENV) pip freeze
	Genshi==0.7
	Trac==1.2
	
	(ENV) pip freeze > requirement.txt
	
	(ENV) pip install -r requirement.txt 
	Requirement already satisfied: Genshi==0.7 in ./ENV/lib/python2.7/site-packages (from -r requirement.txt (line 1))
	Requirement already satisfied: Trac==1.2 in ./ENV/lib/python2.7/site-packages (from -r requirement.txt (line 2))
	Requirement already satisfied: setuptools>=0.6 in ./ENV/lib/python2.7/site-packages (from Trac==1.2->-r requirement.txt (line 2))

