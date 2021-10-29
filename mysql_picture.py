"""
MySQL存图片

"""

import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()

# with open('test.jpg', 'rb') as fd:
#     date = fd.read()
#
# sql = "insert into picture values (1,'test.jpg',%s);"
#
# cur.execute(sql, [date])
# db.commit()

# 获取文件
sql = "select * from picture where filename='test.jpg';"
cur.execute(sql)
date = cur.fetchone()
with open(date[1], 'wb') as fd:
    fd.write(date[2])

cur.close()
db.close()
