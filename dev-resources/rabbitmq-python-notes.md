RabbitMQ Python Client记录

# 1 [pika](https://pika.readthedocs.org)
	
> Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.
	
	
	$ sudo pip install pika
	
	
# 2 Code Fragment

	### (1) 创建连接
	connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
	# 处理连接中数据事件
	connection.process_data_events()
	# 关闭链接
	connection.close()
	#  创建信道
	channel = connection.channel()
	
	
	### (2) 声明队列
	channel.queue_declare(queue = '<queue-name>')
	# 持久化的队列
	channel.queue_declare(queue = '<queue-name>', durable = True)
	# 只允许当前连接访问的队列, 同时获取生成的队列名称
	result = channel.queue_declare(exclusive = True)  
	queue_name = result.method.queue
	
	
	### (3) 声明路由(exchange), <exchange-type>取值为fanout, direct, topic
	channel.exchange_declare(exchange = _exchange_name, exchange_type = '<exchange-type>')
	
	
	### (4) 将队列绑定到路由
	channel.queue_bind( queue = '<queue-name>', exchange = '<exchange-name.', routing_key = '<routing-key>')
	
	
	### (5) 生产消息
	channel.basic_publish(exchange = '<exchange-name>', routing_key = '<routing-key>', body = '<message>')
	# 持久化的消息
	channel.basic_publish(exchange = '<exchange-name>', routing_key = '<routing-key>', body = '<message>'
	    properties = pika.BasicProperties(delivery_mode = 2))

	
	### (6) 消费消息
	channel.basic_consume(consumer_callback, queue = '<queue-name>')
	# 消费消息, 不确认
	channel.basic_consume(consumer_callback, queue = '<queue-name>', no_ack = True)
	# 处理消息
	def consumer_callback(channel, method, properties, body):
	    """         channel: BlockingChannel
	                method: spec.Basic.Deliver
	                properties: spec.BasicProperties
	                body: str or unicode
	    """
	    # 确认消息
	    # channel.basic_ack(delivery_tag = method.delivery_tag)
	    print 'receive message(%s)' % body
	# 开始消费消息
	channel.start_consuming()
	# 设置预取消息数量
	channel.basic_qos(prefetch_count = 1)
	
	### (7) 设置回复信道和相关性ID
	## (7.1) 生产者->消费者
	result = channel.queue_declare(exclusive = True)
	callback_queue_name = result.method.queue
	corr_id = str(uuid.uuid4())
	channel.basic_publish(
            exchange = '', # 默认路由
            routing_key = '<queue-name>',
            properties = pika.BasicProperties( # 设置回复信道和相关性ID
                reply_to = self.callback_queue_name,
                correlation_id = corr_id),
            body = '<message>')
	# -> 消费者
	channel.basic_consume(on_response, queue = callback_queue_name, no_ack = True)
    def on_response(self, channel, method, properties, body):
        if corr_id == properties.correlation_id: # 更具相关性ID获取响应
            response = body
	
	## (7.2) 消费者->生产者
	channel.basic_consume(on_request, queue = '<queue-name>')
	# -> 生产者
	def on_request(channel, method, properties, body):
            n = int(body)
            response = _fib(n)

            # 查找路由键, 同时原样返回相关性ID
            channel.basic_publish(
                exchange = '',
                routing_key = properties.reply_to,
                properties = pika.BasicProperties(correlation_id = properties.correlation_id),
                body = str(response) # 响应
            )
            channel.basic_ack(delivery_tag = method.delivery_tag)
	