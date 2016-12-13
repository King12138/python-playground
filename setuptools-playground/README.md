
REF [Python包管理工具setuptools详解](http://yansu.org/2013/06/07/learn-python-setuptools-in-detail.html).

# 1 创建简单的包

	tmp
	└── demo
	    └── setup.py

	# 打包
	$ python setup.py bdist_egg

	tmp
	└── demo
	    ├── build
	    │   └── bdist.macosx-10.10-intel
	    ├── demo.egg-info
	    │   ├── PKG-INFO
	    │   ├── SOURCES.txt
	    │   ├── dependency_links.txt
	    │   └── top_level.txt
	    ├── dist
	    │   └── demo-0.1-py2.7.egg
	    └── setup.py
	    
	$ file dist/demo-0.1-py2.7.egg 
	dist/demo-0.1-py2.7.egg: Zip archive data, at least v2.0 to extract

# 2 在包中添加内容
	
	tmp/
	└── demo
	    ├── demo
	    │   └── __init__.py
	    ├── setup.py

	# 打包
	$ python setup.py bdist_egg
	# 发布
	$ sudo python setup.py install
	
	# 发布后测试脚本见tmp/demotest/demo_test.py

# 3 进阶

版本改至0.2.

	tmp
	├── demo
	│   ├── setup.py
	│   ├── src
	│   │   ├── demo
	│   │   │   ├── README.txt
	│   │   │   ├── __init__.py
	│   │   │   └── data
	│   │   │       ├── data.bin
	│   │   │       └── data.txt
	│   │   └── tests
	│   │       └── TEST_README.txt

	# 打包
	
	tmp
	├── demo
	│   ├── build
	│   │   ├── bdist.macosx-10.10-intel
	│   │   └── lib
	│   │       └── demo
	│   │           ├── README.txt
	│   │           ├── __init__.py
	│   │           └── data
	│   │               └── data.bin
	│   ├── dist
	│   │   └── demo-0.2-py2.7.egg
	│   ├── setup.py
	│   ├── src
	│   │   ├── demo
	│   │   │   ├── README.txt
	│   │   │   ├── __init__.py
	│   │   │   └── data
	│   │   │       ├── data.bin
	│   │   │       └── data.txt
	│   │   ├── demo.egg-info
	│   │   │   ├── PKG-INFO
	│   │   │   ├── SOURCES.txt
	│   │   │   ├── dependency_links.txt
	│   │   │   └── top_level.txt
	│   │   └── tests
	│   │       └── TEST_README.txt
	
	# 发布
	
# 4 使用entry_points

功能:

+ (1) 动态发现服务和插件: 还是看官方文档吧.
+ (2) 自动生成脚本: console_scripts, gui_scripts, eggsecutable	


# 5 stevedore



	
	