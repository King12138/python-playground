# 查看表名
SELECT TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='test';
# 查看表中字段
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_COMMENT
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA='python_playground'  AND TABLE_NAME='COOKIES'
ORDER BY COLUMN_NAME -- ORDINAL_POSITION
;

select * from USERS;
select * from COOKIES;
select * from LINE_ITEMS;
select * from ORDERS;
select * from EMPLOYEE;

# 用户cookiemon下的订单详情
select o.order_id, u.username, u.phone, c.cookie_name, li.quantity, li.extended_cost
from ORDERS o
	inner join USERS u on o.user_id = u.user_id
    inner join LINE_ITEMS li on li.order_id = o.order_id
    inner join COOKIES c on li.cookie_id = c.cookie_id
where u.username = 'cookiemon'
;    

