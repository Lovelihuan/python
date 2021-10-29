"""
MySQL 插入 修改 删除
"""


import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()

name = input("姓名：")
age = input("年龄：")
sex = input("男或女?")
score = input("成绩：")

qdl = "insert into class (姓名,年龄,性别,成绩) values (%s,%s,%s,%s);"

cur.execute(qdl, [name, age, sex, score])
db.commit()

rr = "select * from class;"
cur.execute(rr)
# date = cur.fetchone()
# print(date)
date = cur.fetchmany(2)
print(date)

cur.close()
db.close()
