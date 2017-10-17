# 查看表名
SELECT TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='python_playground';
# 查看表中字段
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_COMMENT
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA='python_playground'  AND TABLE_NAME='polls_question'
ORDER BY COLUMN_NAME -- ORDINAL_POSITION
;


select * from polls_question;
select * from polls_choice;
