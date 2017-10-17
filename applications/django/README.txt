######################################################
安装
######################################################

$ pip3 install Django
$ python3
>>> import django
>>> django.__version__
'1.11.6'

######################################################
创建项目和应用
######################################################

创建项目mysite
$ django-admin startproject mysite
$ tree
.
└── mysite
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

启动开发服务器: 
$ cd mysite/
$ python3 manage.py runserver
访问: http://127.0.0.1:8000/

启动应用: python3 manage.py startapp [app_label]

在项目下创建应用polls
$ python3 manage.py startapp polls
$ tree
.
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py


######################################################
数据库: MySQL
######################################################

###mysite/settings.py
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python_playground',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

### mysqlclient
mysqlclient is a fork of MySQL-python. It adds Python 3 support and fixed many bugs.
https://pypi.python.org/pypi/mysqlclient/1.3.12
安装: $ pip3 install mysqlclient

### 执行生成数据库迁移记录
$ python3 manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Choice
    - Create model Question
    - Add field question to choice
副作用: 在数据库中生成表django_migrations    

### 查看迁移记录中SQL
$ python3 manage.py sqlmigrate polls 0001
BEGIN;
--
-- Create model Choice
--
CREATE TABLE `polls_choice` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `choice_text` varchar(200) NOT NULL, `votes` integer NOT NULL);
--
-- Create model Question
--
CREATE TABLE `polls_question` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `question_text` varchar(200) NOT NULL, `pub_date` datetime(6) NOT NULL);
--
-- Add field question to choice
--
ALTER TABLE `polls_choice` ADD COLUMN `question_id` integer NOT NULL;
ALTER TABLE `polls_choice` ADD CONSTRAINT `polls_choice_question_id_c5b4b260_fk_polls_question_id` FOREIGN KEY (`question_id`) REFERENCES `polls_question` (`id`);
COMMIT;

### 执行迁移
$ python3 manage.py migrate
System check identified some issues:

WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
	HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/1.11/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK


副作用: 生成表
'auth_group'
'auth_group_permissions'
'auth_permission'
'auth_user'
'auth_user_groups'
'auth_user_user_permissions'
'django_admin_log'
'django_content_type'
'django_session'
'polls_choice'
'polls_question'


######################################################
Manage Shell
######################################################
$ python3 manage.py shell
>>> from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet []>
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
1
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2017, 10, 16, 8, 18, 53, 839348, tzinfo=<UTC>)
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()
<QuerySet [<Question: Question object>]>

[...外键相关的操作...]
   
######################################################
admin
######################################################
$ python3 manage.py createsuperuser
Username (leave blank to use 'jiedong'): admin
Email address: admin@example.co
Password: fuck1234

$ python3 manage.py runserver
访问: http://127.0.0.1:8000/admin/ 

######################################################
测试
######################################################
测试应用
$ python3 manage.py test polls



