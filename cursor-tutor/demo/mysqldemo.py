import mysql.connector

# 数据库连接配置
config = {
    "user": "root",
    "password": "itech4u123",
    "host": "10.101.32.33",
    "database": "itech4u",
    "port": 30306, 
}


# 连接到数据库
connection = mysql.connector.connect(**config)

# 创建一个游标对象
cursor = connection.cursor()

# SQL 查询语句，添加 LIMIT 100 以仅查询前 100 条数据
# query = "SELECT application_no, abstract FROM `patent-20230322` WHERE patent_type = '中国实用新型专利授权公告标准化全文文本数据' ORDER BY RAND() LIMIT 20;"
query = '''
SELECT application_no, abstract
FROM `patent-20230322`
WHERE patent_type = '中国实用新型专利授权公告标准化全文文本数据'
AND technical_field LIKE '%机器人%'
ORDER BY RAND()
LIMIT 20'''


# 执行查询
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()

# 打印查询结果
for row in results:
    application_no, abstract = row
    print(f"Application No: {application_no}, Abstract: {abstract}")

# 关闭游标和数据库连接
cursor.close()
connection.close()
