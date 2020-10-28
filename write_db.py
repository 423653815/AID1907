'''
写操作演示
insert update delete
'''
import pymysql
db = pymysql.connect(host='192.168.142.133',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()

# name = input('Name:')
# age = input('Age:')
# score = input('Score:')

try:
    #插入操作
    #合成一个正确的sql语句才能正确commit
    # sql = "insert into class_1 (name,age,score) values ('%s',%s,%s)" % (name,age,score)

    #sql语句值参量可以通过execute传入
    # sql = "insert into class_1 (name,age,score) values (%s,%s,%s)"
    # cur.execute(sql,[name,age,score])#执行语句

    #修改操作
    sql = "update class_1 set score=91 where name='Lucy'"
    cur.execute(sql)

    #删除操作
    sql = "delete from class_1 where name = 'Jim'"
    cur.execute(sql)

    db.commit()#同步数据库
except Exception as e:
    print(e)
    db.rollback() #回滚到没有commit之前的状态
cur.close()
db.close()