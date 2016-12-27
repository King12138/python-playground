RabbitMQ基本概念和配置记录

# 0 资源

[RabbitMQ文档](http://www.rabbitmq.com/documentation.html)

## 0.1 [服务端文档](http://www.rabbitmq.com/admin-guide.html)

+ 配置服务器
+ 管理和监控: 管理插件和`rabbitmqctl`
+ 集群和HA
+ 操作
+ 开发和问题排解 


# 1 [下载和安装](http://www.rabbitmq.com/download.html)
	
	# Mac
	$ brew update
	$ brew install rabbitmq
	......
	wxmac-3.0.2_4
	erlang-19.2
	rabbitmq-server/v3.6.4
	......
	/usr/local/Cellar/rabbitmq/3.6.4
	......
	
	# 启动
	$ export PATH=/usr/local/sbin:$PATH
	$ rabbitmq-server
	# 后台进程方式运行
	$ rabbitmq-server -detached
	# The broker creates a user guest with password guest.
	
	RabbitMQ 3.6.4. Copyright (C) 2007-2016 Pivotal Software, Inc.
	  ##  ##      Licensed under the MPL.  See http://www.rabbitmq.com/
	  ##  ##
	  ##########  Logs: /usr/local/var/log/rabbitmq/rabbit@localhost.log
	  ######  ##        /usr/local/var/log/rabbitmq/rabbit@localhost-sasl.log
	  ##########
	              Starting broker...
	 completed with 10 plugins.
	
	$ ps -ef | grep rabbit
	  501 14626 14540   0  7:41下午 ttys000    0:07.70 /usr/local/Cellar/erlang/19.2/lib/erlang/erts-8.2/bin/beam.smp -W w -A 64 -P 1048576 -t 5000000 -stbt db -K true -B i -- -root /usr/local/Cellar/erlang/19.2/lib/erlang -progname erl -- -home /Users/xxx -- -pa /usr/local/Cellar/rabbitmq/3.6.4/ebin -noshell -noinput -s rabbit boot -sname rabbit@localhost -boot /usr/local/opt/erlang/lib/erlang/bin/start_clean -kernel inet_default_connect_options [{nodelay,true}] -rabbit tcp_listeners [{"127.0.0.1",5672}] -sasl errlog_type error -sasl sasl_error_logger false -rabbit error_logger {file,"/usr/local/var/log/rabbitmq/rabbit@localhost.log"} -rabbit sasl_error_logger {file,"/usr/local/var/log/rabbitmq/rabbit@localhost-sasl.log"} -rabbit enabled_plugins_file "/usr/local/etc/rabbitmq/enabled_plugins" -rabbit plugins_dir "/usr/local/Cellar/rabbitmq/3.6.4/plugins" -rabbit plugins_expand_dir "/usr/local/var/lib/rabbitmq/mnesia/rabbit@localhost-plugins-expand" -os_mon start_cpu_sup false -os_mon start_disksup false -os_mon start_memsup false -mnesia dir "/usr/local/var/lib/rabbitmq/mnesia/rabbit@localhost" -kernel inet_dist_listen_min 25672 -kernel inet_dist_listen_max 25672
	
	# 停止
	$ rabbitmqctl stop
	
	
管理插件: [Management Plugin](http://www.rabbitmq.com/management.html), 开启后访问`http://localhost:15672/`.
	
# 2 [配置](http://www.rabbitmq.com/configure.html)

三种配置方式:

+ [环境变量](http://www.rabbitmq.com/configure.html#define-environment-variables)
+ [配置文件](http://www.rabbitmq.com/configure.html#configuration-file)
+ [运行时参数](http://www.rabbitmq.com/parameters.html)


环境配置rabbitmq-env.conf: `/usr/local/etc/rabbitmq/rabbitmq-env.conf`.

配置文件rabbitmq.config(标准Erlang配置文件): `/usr/local/etc/rabbitmq/rabbitmq.config`.

	/usr/local/var/log/rabbitmq/rabbit@localhost.log: 
	
	=INFO REPORT==== 20-Dec-2016::19:41:09 ===
	node           : rabbit@localhost
	home dir       : /Users/xxx
	config file(s) : /usr/local/etc/rabbitmq/rabbitmq.config (not found)
	cookie hash    : iK0bNXP8sZ6JpQr1NqQhHQ==
	log            : /usr/local/var/log/rabbitmq/rabbit@localhost.log
	sasl log       : /usr/local/var/log/rabbitmq/rabbit@localhost-sasl.log
	database dir   : /usr/local/var/lib/rabbitmq/mnesia/rabbit@localhost
	......

示例配置见[rabbitmq.config.example](https://github.com/rabbitmq/rabbitmq-server/blob/master/docs/rabbitmq.config.example).




