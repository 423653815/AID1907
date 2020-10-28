import pymysql
class User():
    def __init__(self,username,password):
        self.username = username
        self.password = password
class UserHandle():
    def __init__(self):
        self.db = pymysql.connect.connect(host='192.168.142.133',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
    def login(user):
        pass
    def regist(user):
        pass

def home_page():
    print('1 - 登录')
    print('2 - 注册')
def main():
    order = input('请输入')
    if order == '1':
        print('用户登录,请输入用户名密码')
        username = input('用户名:')
        password = input('密码:')


if __name__ == '__main__':
    main()