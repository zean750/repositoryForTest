import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='19870605s',
    auth_plugin='mysql_native_password',
    database = 'zeantest'
)
# print(mydb)
mycursor = mydb.cursor()

# mycursor.execute('SHOW DATABASES ')
# for i in mycursor:
#     print(i)

# mycursor.execute('CREATE TABLE customers (name varchar(255),address varchar(255))')
# mycursor.execute('ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')

# sql = 'INSERT INTO customers(name,address) VALUES (%s,%s)'
# val = ('John','Highway 21') 
# 多行的时候用数组包起来
# mycursor.execute(sql,val)
# # 注意需要提交
# mydb.commit()
# print(mycursor.rowcount,'record inserted!')

# mycursor.execute('SELECT * FROM customers')
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)



