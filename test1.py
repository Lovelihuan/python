import pymysql

db = pymysql.connect(host='localhost',
                     port=3306, user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
c = db.cursor()

c.execute("insert into class values(9,'aslf',17,'女',110,'wwerew');")
db.commit()

c.close()
db.close()
