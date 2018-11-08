import pymysql

#db = pymysql.connect('localhost' , 'root' ,'root' , 'mytest')
#host=None, user=None, password="",database=None, port=0
db = pymysql.connect(host='localhost' , user='root' ,password='root' , database='mytest' , port=3306)

cursor = db.cursor()

cursor.execute('select version()')

data = cursor.fetchone()

print('database version: %s' % data)

db.close()