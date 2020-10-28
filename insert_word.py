import re
import pymysql
#连接数据库
db = pymysql.connect(host='192.168.142.133',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

#获取游标（操作数据库，执行sql语句，得到执行结果）
cur = db.cursor()


file = open('dict.txt')
sql = 'insert into words (word,mean) values (%s,%s)'
for line in file:
    # tmp = line.split(' ',1)
    # word = tmp[0]
    # mean = tmp[1].strip()
    # cur.execute(sql,[word,mean])
    tup = re.findall(r'(\S+)\s+(.*)',line)
    print(tup)
    cur.execute(sql,tup[0])

try:
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


cur.close()
db.close()