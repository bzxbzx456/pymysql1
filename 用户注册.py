from hashlib import sha1
import pymysql
from settings import dbparams
import datetime


conn = pymysql.connect(**dbparams)
cursor = conn.cursor()

try:
    username = input("请输入你的用户名：")
    password = input("请输入你的密码：")
    password = sha1(password.encode('utf8')).hexdigest()
    email = input("请输入你的邮箱：")

    if len(username)<2 or username.isspace():
        print("用户名长度不能小于2")
        exit()

    result = cursor.execute("select * from user where username='{}'".format(username))
    if result > 0:
        print("重新输入username")
        exit()

    sql = "insert into user (username,password,regtime,email) values ('{}','{}','{}','{}') ".format(username,password,datetime.datetime.now(),email)

    print(sql)
    result = cursor.execute(sql)
    conn.commit()
    print(result)

except Exception as e:
    print(e)
    conn.rollback()
finally:
    # 4.关闭游标
    cursor.close()
    conn.close()
