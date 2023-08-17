# mysql connect package
# pip --> conda
import pymysql


# connect Mysql
# ip, port, username, password, database name
ip = 'localhost'
port = '3306'
username = 'yojulab'
password = '!yojulab*'
database = 'db_cars'

# editor = statement
connect = pymysql.connect(host = ip, user = username, password = password, database= database)

# make select query
sql_query = 'select * from car_infors;'

# execute select query
import pandas

# return resultset
df = pandas.read_sql(sql = sql_query, con = connect)

# return resultset and then display

# close
connect.close()

pass

