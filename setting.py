dbparams = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'4866098',
    'port':3306,
    'db':'homework_student',
    'charset':'utf8'
}

import pymysql

conn = pymysql.Connect(**dbparams)
cursor = conn.cursor()
sql = "CREATE DATABASE IF NOT EXISTS bbs default charset=utf8"
cursor.execute(sql)
cursor.close()
conn.close()