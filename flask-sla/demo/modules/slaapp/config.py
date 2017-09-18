import pymysql

db_config = {
          'host':'115.159.19.87',
          'port':3306,
          'user':'root',
          'password':'weimob@123',
          'db':'count_sla',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }