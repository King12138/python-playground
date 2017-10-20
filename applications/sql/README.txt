######################################################
MySQLdb
######################################################

MySQLdbOps.py


######################################################
SQLAlchemy
######################################################

pip install SQLAlchemy==1.1.14
pip install --upgrade SQLAlchemy==1.1.14

$ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.1.14'


$ sudo pip install mock
Password:
The directory '/Users/jiedong/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/jiedong/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting mock
  Downloading mock-2.0.0-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 181kB/s 
Collecting funcsigs>=1; python_version < "3.3" (from mock)
  Downloading funcsigs-1.0.2-py2.py3-none-any.whl
Requirement already satisfied: six>=1.9 in /Library/Python/2.7/site-packages (from mock)
Collecting pbr>=0.11 (from mock)
  Downloading pbr-3.1.1-py2.py3-none-any.whl (99kB)
    100% |████████████████████████████████| 102kB 50kB/s 
Installing collected packages: funcsigs, pbr, mock
Successfully installed funcsigs-1.0.2 mock-2.0.0 pbr-3.1.1

$ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mock
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Python/2.7/site-packages/mock/__init__.py", line 2, in <module>
    import mock.mock as _mock
  File "/Library/Python/2.7/site-packages/mock/mock.py", line 68, in <module>
    from six import wraps
ImportError: cannot import name wraps
>>> exit()

>>> 解决方法: 查询出实际使用的six的版本与安装的版本不一致, 因lib/python目录的存在, 直接删除掉.
/System/Library/Frameworks/Python.framework/Versions/Current/Extras



