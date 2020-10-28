'''
pymysql 操作数据库基本流程
'''
import pymysql
#连接数据库
db = pymysql.connect(host='192.168.142.133',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

#获取游标（操作数据库，执行sql语句，得到执行结果）
cur = db.cursor()

#执行语句
sql = "insert into class_1 values(6,'Emma',17,'w',19)"
cur.execute(sql)#执行语句
#提交到数据库
db.commit()
#关闭游标
cur.close()
#关闭数据库
db.close()
