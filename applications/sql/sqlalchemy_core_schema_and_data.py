# -*- coding: utf-8 -*-

'''
Created on 2017-10-19 18:10:59
SQLAlchemy Core schema定义
@author: zhoujiagen
'''
from datetime import datetime

# 索引, 外键
from sqlalchemy import Index, ForeignKey
# 字段数据类型
from sqlalchemy import Integer, Numeric, String, DateTime, Boolean
# 元数据
from sqlalchemy import MetaData
# 约束
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint, ForeignKeyConstraint
# 表和列
from sqlalchemy import Table, Column

metadata = MetaData()
# 表COOKIES
cookies = Table("COOKIES", metadata,
        Column("cookie_id", Integer(), primary_key = True),
        Column("cookie_name", String(50)),  # index = True
        Column("cookie_recipe_url", String(255)),
        Column("cookie_sku", String(55)),
        Column("quantity", Integer()),
        Column("unit_cost", Numeric(12, 2)),
        # 检查约束
        CheckConstraint("unit_cost >= 0.0", name = "unit_cost_positive"),
        # 索引
        Index("ix_cookies_cookie_name", "cookie_name"),
        Index("ix_cookie_sku_name", "cookie_sku", "cookie_name")
)
# Index("ix_cookies_cookie_name", cookies.c.cookie_name)  # 使用Table中字段
# Index("ix_cookie_sku_name", cookies.c.cookie_sku, cookies.c.cookie_name)

# 表USERS
users = Table("USERS", metadata,
        Column("user_id", Integer()),  # primary_key = True
        Column("username", String(15), nullable = False),  # unique = True
        Column("email_address", String(255), nullable = False),
        Column("phone", String(20), nullable = False),
        Column("password", String(25), nullable = False),
        Column("create_on", DateTime(), default = datetime.now),
        Column("update_on", DateTime(), default = datetime.now, onupdate = datetime.now),
        # 主键约束
        PrimaryKeyConstraint("user_id", name = "user_pk"),
        # 唯一性约束
        UniqueConstraint("username", name = "uix_username"),
 )


# 表ORDERS
orders = Table("ORDERS", metadata,
        Column("order_id", Integer, primary_key = True),
        Column("user_id", ForeignKey("USERS.user_id")),  # 外键
        Column("shipped", Boolean(), default = False)
)

# 表LINE_ITEMS
line_items = Table("LINE_ITEMS", metadata,
        Column("line_items_id", Integer(), primary_key = True),
        Column("order_id"),  # ForeignKey("ORDERS.order_id")
        Column("cookie_id", ForeignKey("COOKIES.cookie_id")),  # 外键
        Column("quantity", Integer()),
        Column("extended_cost", Numeric(12, 2)),
        # 外键约束
        ForeignKeyConstraint(["order_id"], ["ORDERS.order_id"])
)

# 表EMPLOYEE
employee = Table("EMPLOYEE", metadata,
    Column("id", Integer(), primary_key = True),
    Column("manager", None, ForeignKey("EMPLOYEE.id")),
    Column("name", String(255), unique = True)
)


def force_create_schema(metadata, engine):
    """创建Schema"""
    metadata.drop_all(engine)  # 清理
    metadata.create_all(engine)  # 创建

def init_data(connection):
    """初始化测试数据"""
    from sqlalchemy import insert

    # users数据
    users_list = [
        {
            'username': 'cookiemon',
            'email_address': 'mon@cookie.com',
            'phone': '111-111-1111',
            'password': 'password'
        }, {
            'username': 'cakeeater',
            'email_address': 'cakeeater@cake.com',
            'phone': '222-222-2222',
            'password': 'password'
        }, {
            'username': 'pieguy',
            'email_address': 'guy@pie.com',
            'phone': '333-333-3333',
            'password': 'password'
        }
    ]

    ins = insert(users)
    result = connection.execute(ins, users_list)
    print result

    # cookies数据
    cookies_list = [
        {
            'cookie_name': 'chocolate chip',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html',
            'cookie_sku': 'CC01',
            'quantity': '12',
            'unit_cost': '0.50'
        },
        {
            'cookie_name': 'dark chocolate chip',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe_dark.html',
            'cookie_sku': 'CC02',
            'quantity': '1',
            'unit_cost': '0.75'
        },
        {
            'cookie_name': 'peanut butter',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'PB01',
            'quantity': '24',
            'unit_cost': '0.25'
        },
        {
            'cookie_name': 'oatmeal raisin',
            'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'EWW01',
            'quantity': '100',
            'unit_cost': '1.00'
        }
    ]
    ins = insert(cookies)
    result = connection.execute(ins, cookies_list)
    print result

    # orders, line_items数据
    ins = insert(orders).values(user_id = 1)
    result = connection.execute(ins)
    order_id = result.inserted_primary_key
    line_items_list = [
        {
            'order_id': order_id,
            'cookie_id': 1,
            'quantity': 2,
            'extended_cost': 1.00
        },
        {
            'order_id': order_id,
            'cookie_id': 3,
            'quantity': 12,
            'extended_cost': 3.00
        }
    ]
    connection.execute(insert(line_items), line_items_list)

    ins = insert(orders).values(user_id = 2)
    result = connection.execute(ins)
    order_id = result.inserted_primary_key
    line_items_list = [
        {
            'order_id': order_id,
            'cookie_id': 1,
            'quantity': 24,
            'extended_cost': 12.00
        },
        {
            'order_id': order_id,
            'cookie_id': 4,
            'quantity': 6,
            'extended_cost': 6.00
        }
    ]
    connection.execute(insert(line_items), line_items_list)

    # employee数据
    ins = insert(employee).values(name = "MGR")
    result = connection.execute(ins)
    employee_mgr_id = result.inserted_primary_key
    employee_list = [
        {
            'name': 'Alice',
            'manager': employee_mgr_id
        },
        {
            'name': 'Bob',
            'manager': employee_mgr_id
        }
    ]
    connection.execute(insert(employee), employee_list)

def _insert(connection):
    """插入"""
    print hasattr(cookies, "insert")  # True

    # 这种方式IDE中报错, 但可执行
#     ins = cookies.insert().values(
#         cookie_name = "chocolate chip",
#         cookie_recipe_url = "http://some.aweso.me/cookie/recipe.html",
#         cookie_sku = "CC01",
#         quantity = "12",
#         unit_cost = "0.50"
#     )
    from sqlalchemy import insert
    ins = insert(cookies).values(
        cookie_name = "chocolate chip",
        cookie_recipe_url = "http://some.aweso.me/cookie/recipe.html",
        cookie_sku = "CC01",
        quantity = "12",
        unit_cost = "0.50"
    )
    # 生成的SQL
    print str(ins)
    # SQL中占位符参数
    print ins.compile().params
    # 执行
    result = connection.execute(ins)
    print result  # sqlalchemy.engine.result.ResultProxy
    print result.inserted_primary_key  # 主键

    # 批量插入
    ins = insert(cookies)
    cookie_list = [
        {
            'cookie_name': 'peanut butter',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'PB01',
            'quantity': '24',
            'unit_cost': '0.25'
        },
        {
            'cookie_name': 'oatmeal raisin',
            'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'EWW01',
            'quantity': '100',
            'unit_cost': '1.00'
        }
    ]
    connection.execute(ins, cookie_list)  # 执行时传入参数


def _query(connection):
    """查询"""
    from sqlalchemy import select
    s = select([cookies])
    print (str(s), s.compile().params)
    rp = connection.execute(s)  # 结果代理(ResultProxy)
    results = rp.fetchall()
    for row in results:
        print row
        # 访问字段
        print (row[0], row.cookie_name)
        # print row[cookies.c.cookie_name] # IDE报错但可执行
    print

    # 选择列
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    # 排序
    # s = s.order_by(cookies.c.quantity)
    # 倒序
    from sqlalchemy import desc
    s = s.order_by(desc(cookies.c.quantity))
    # 限制返回结果集
    s = s.limit(2)
    print (str(s), s.compile().params)
    rp = connection.execute(s)
    print rp.keys()
    for row in  rp.fetchall():
        print row
    print

    # 内建函数
    # from sqlalchemy.sql import func
    from sqlalchemy import func
    s = select([func.sum(cookies.c.quantity)])
    rp = connection.execute(s)
    # print rp.scalar()  # 标量
    result = rp.first()
    print (result.keys(), result.sum_1)  # 默认列名为<func_name>_<position>
    # 别名
    s = select([func.count(cookies.c.cookie_name).label("inventory_count")])
    rp = connection.execute(s)
    result = rp.first()
    print (result.keys(), result.inventory_count)
    print

    # 过滤
    s = select([cookies]).where(cookies.c.cookie_name == "chocolate chip")
    rp = connection.execute(s)
    result = rp.first()
    print (result, result.keys(), result.items())  # 结果/键/键值
    # 子句元素中方法
    s = select([cookies]).where(cookies.c.cookie_name.like("%chocolate%"))
    rp = connection.execute(s)
    for row in rp.fetchall():
        print row.cookie_name
    print

    # 操作符
    s = select([cookies.c.cookie_name, "SKU-" + cookies.c.cookie_sku])
    rp = connection.execute(s)
    for row in rp:  # 直接在ResultProxy上迭代
        print row
    print
    from sqlalchemy import cast
    s = select([cookies.c.cookie_name,
                cast((cookies.c.quantity * cookies.c.unit_cost), Numeric(12, 2)).label("inv_cost")])
    rp = connection.execute(s)
    for row in rp:
        print row.items()
    #  布尔操作符
    from sqlalchemy import and_, or_
    s = select([cookies]).where(
        and_(
            cookies.c.quantity > 23,
            cookies.c.unit_cost < 0.40
        )
    )
    print str(s), s.compile().params
    rp = connection.execute(s)
    for row in rp:
        print (row.cookie_name, row.quantity, row.unit_cost)
    print
    s = select([cookies]).where(
        or_(
            cookies.c.quantity.between(10, 50),
            cookies.c.cookie_name.contains("chip")
        )
    )
    print str(s), s.compile().params
    rp = connection.execute(s)
    for row in rp:
        print (row.cookie_name, row.quantity)
    print

def _update(connection):
    """更新"""
    from sqlalchemy import update
    u = update(cookies).where(cookies.c.cookie_name == "chocolate chip")
    u = u.values(quantity = (cookies.c.quantity + 120))
    result = connection.execute(u)
    print result, result.rowcount  # 影响的行数

def _delete(connection):
    """删除"""
    from sqlalchemy import delete
    d = delete(cookies).where(cookies.c.cookie_name == "dark chocolate chip")
    result = connection.execute(d)
    print result, result.rowcount

def _join(connection):
    """联接"""
    from sqlalchemy import select
    columns = [orders.c.order_id, users.c.username, users.c.phone,
               cookies.c.cookie_name, line_items.c.quantity, line_items.c.extended_cost]
    # 用户cookiemon下的订单详情
    cookiemon_orders = select(columns).select_from(
        orders.join(users, onclause = orders.c.user_id == users.c.user_id)
            .join(line_items, onclause = line_items.c.order_id == orders.c.order_id)
            .join(cookies, onclause = line_items.c.cookie_id == cookies.c.cookie_id)
        ).where(users.c.username == 'cookiemon')
    print str(cookiemon_orders), cookiemon_orders.compile().params
    rp = connection.execute(cookiemon_orders)
    for row in rp:
        print row
    print

    # 用户下的订单数量
    from sqlalchemy import func
    columns = [users.c.username, func.count(orders.c.order_id)]
    all_orders = select(columns).select_from(users.outerjoin(orders)).group_by(users.c.username)  # 分组
    print str(all_orders), all_orders.compile().params
    rp = connection.execute(all_orders)
    for row in rp:
        print row

def _alias(connection):
    """别名"""
    from sqlalchemy import select, and_

    # 查询雇员及其上级
    mgr = employee.alias("mgr")
    s = select([employee.c.name, mgr.c.name],
               and_(employee.c.manager == mgr.c.id, mgr.c.name == "MGR"))
    print str(s), s.compile().params
    rp = connection.execute(s)
    for row in rp:
        print row

def _chaining(connection):
    """链式调用"""
    _get_orders_by_user(connection, 'cakeeater')
    _get_orders_by_user(connection, 'cakeeater', details = True)
    _get_orders_by_user(connection, 'cakeeater', shipped = True)
    _get_orders_by_user(connection, 'cakeeater', shipped = False)
    _get_orders_by_user(connection, 'cakeeater', shipped = False, details = True)

def _get_orders_by_user(connection, username, shipped = None, details = False):
    """"按用户查询订单, 展示条件化的链式调用"""
    from sqlalchemy import select
    columns = [orders.c.order_id, users.c.username, users.c.phone]
    joins = users.join(orders)
    if details:
        columns.extend([cookies.c.cookie_name, line_items.c.quantity,
                       line_items.c.extended_cost])
        joins = joins.join(line_items).join(cookies)
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(joins)
    cust_orders = cust_orders.where(users.c.username == username)

    if shipped is not None:
        cust_orders = cust_orders.where(orders.c.shipped == shipped)

    print "DEBUG>>> ", str(cust_orders), cust_orders.compile().params, "\n"

    result = connection.execute(cust_orders).fetchall()
    return result

def _raw_query(connection):
    """使用原生SQL查询"""
    result = connection.execute("SELECT * FROM ORDERS").fetchall();
    print result
    print

    from sqlalchemy import select, text
    s = select([users]).where(text("username='cookiemon'"))
    print str(s), s.compile().params
    result = connection.execute(s).fetchall()
    print result

def _handle_exception(connection):
    """处理异常"""
    from sqlalchemy import select, insert
    from sqlalchemy.exc import IntegrityError

    s = select([users.c.username])
    rp = connection.execute(s)
    for row in rp:
        try:
            print row.username, row.password
        except AttributeError as e:
            print e

    s = select([users.c.username]).where(users.c.username == 'cookiemon')
    for row in connection.execute(s):
        print row
    try:
        connection.execute(insert(users).values(username = 'cookiemon'))
    except IntegrityError as e:
        print (e, e.orig.message, e.params)


def _handle_tx(connection):
    """处理事务"""
    from sqlalchemy import select, update
    from sqlalchemy.exc import IntegrityError

    _order_id = 1

    s = select([line_items.c.cookie_id, line_items.c.quantity]).where(line_items.c.order_id == _order_id)

    tx = connection.begin()  # 开启事务
    cookies_to_ship = connection.execute(s).fetchall()
    try:
        for cookie in cookies_to_ship:
            u = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id)
            u = u.values(quantity = cookies.c.quantity - cookie.quantity)  # 更新库存
            result = connection.execute(u)
            print "DEBUG>>> update cookies: ", result.rowcount

        # 更新订单发送状态
        u = update(orders).where(orders.c.order_id == _order_id)
        u = u.values(shipped = True)
        result = connection.execute(u)
        print "DEBUG>>> update orders: ", result.rowcount
        print "orders[id=%s] shipped" % _order_id
        # 提交事务
        tx.commit()
    except IntegrityError as e:
        # 回滚事务
        tx.rollback()
        print e

if __name__ == '__main__':
    # 显示Schema定义
#     print metadata.tables
#     for table in metadata.sorted_tables:
#         print repr(table)

    # 持久化Schema定义
    from sqlalchemy_mysql_connection import get_engine
    engine = get_engine()
    connection = engine.connect()
#     force_create_schema(metadata, engine)

    # 初始化数据
#     init_data(connection)

    # 数据操作
#     _insert(connection)
#     _query(connection)
#     _update(connection)
#     _delete(connection)
#     _join(connection)
#     _alias(connection)
#     _chaining(connection)
#     _raw_query(connection)
#     _handle_exception(connection)
    _handle_tx(connection)


