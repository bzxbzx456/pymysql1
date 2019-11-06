from settings import dbparams
import pymysql



conn = pymysql.Connect(**dbparams)
cursor = conn.cursor()

sql1 = "create table if not exists user " \
       "(" \
       "uid int auto_increment primary key," \
       "username varchar(20) unique not null ," \
       "usertype enum('普通用户','管理员') default '普通用户'," \
       "password varchar(128) not null ," \
       "regtime datetime not null," \
       "email varchar(100)" \
       ")"
cursor.execute(sql1)

cursor.close()
conn.close()