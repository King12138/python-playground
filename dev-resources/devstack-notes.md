DevStack安装和配置

# 1 文档

+ [文档入口](http://docs.openstack.org/developer/devstack/): 提供了默认安装的功能说明.
+ [DevStack概览](http://docs.openstack.org/developer/devstack/overview.html)
+ [配置](http://docs.openstack.org/developer/devstack/configuration.html)
+ [DevStack网络配置](http://docs.openstack.org/developer/devstack/networking.html)
+ [DevStack指南](http://docs.openstack.org/developer/devstack/guides.html): 有contribute时更新.
+ [DevStack插件](http://docs.openstack.org/developer/devstack/plugins.html): 提供额外的服务/特性和配置.

## 2 环境

VirtualBox Version 5.1.10 r112026 (Qt5.6.2), Ubuntu 14.04 LTS; 

虚拟机两个网卡(网络地址转换NAT), Ubuntu中Python版本2.7.12.

Ubuntu ifconfig:

	eth0      Link encap:Ethernet  HWaddr 08:00:27:ef:e1:30  
	          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
	          inet6 addr: fe80::a00:27ff:feef:e130/64 Scope:Link
	          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
	          RX packets:52 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:131 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:1000 
	          RX bytes:6067 (6.0 KB)  TX bytes:15610 (15.6 KB)
	
	eth1      Link encap:Ethernet  HWaddr 08:00:27:f6:0f:f4  
	          inet addr:10.0.3.15  Bcast:10.0.3.255  Mask:255.255.255.0
	          inet6 addr: fe80::a00:27ff:fef6:ff4/64 Scope:Link
	          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
	          RX packets:2 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:48 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:1000 
	          RX bytes:1180 (1.1 KB)  TX bytes:8428 (8.4 KB)
	
	lo        Link encap:Local Loopback  
	          inet addr:127.0.0.1  Mask:255.0.0.0
	          inet6 addr: ::1/128 Scope:Host
	          UP LOOPBACK RUNNING  MTU:65536  Metric:1
	          RX packets:26 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:26 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:0 
	          RX bytes:1926 (1.9 KB)  TX bytes:1926 (1.9 KB)


# 3 安装

local.conf配置:

	[[local|localrc]]
	ADMIN_PASSWORD=zhoujiagen
	DATABASE_PASSWORD=$ADMIN_PASSWORD
	RABBIT_PASSWORD=$ADMIN_PASSWORD
	SERVICE_PASSWORD=$ADMIN_PASSWORD
	PUBLIC_INTERFACE=eth1
	HOST_IP=10.42.0.52
	FLOATING_RANGE=10.42.0.52/24
	PUBLIC_NETWORK_GATEWAY=10.42.0.1
	Q_FLOATING_ALLOCATION_POOL=start=10.42.0.250,end=10.42.0.254

开始安装: `./stack.sh`.

	...
	Need to get 58.8 MB of archives.
	...
