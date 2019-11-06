import pymysql
from hashlib import sha1
from settings import dbparams

conn = pymysql.Connect(**dbparams)
cursor = conn.cursor()
# 输入用户名和密码
username = input("请输入用户名：")
password = input("请输入密码：")
password = sha1(password.encode('utf8')).hexdigest()
print(username,password)

sql = "select uid from user where username= %s and password= %s"
print(sql)

result = cursor.execute(sql,[username,password])
print(result)
print(cursor._executed)

if result>0:
    print("登录成功")
else:
    print("登录失败,重新登录")

cursor.close()
conn.close()