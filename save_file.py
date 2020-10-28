'''
二进制文件存取示例
'''
import pymysql
db = pymysql.connect(host='192.168.142.133',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()

#执行语句
# with open('0.png','rb') as f:
#     data = f.read()

#存入图片
# sql = 'insert into images values (1,%s,%s)'
# cur.execute(sql,[data,'策略模式'])
# db.commit()

#提取图片
sql = "select photo from images where comment='策略模式'"
cur.execute(sql)
data = cur.fetchone()[0]
with open('1.png','wb') as f:
    f.write(data)


#关闭游标
cur.close()

db.close()