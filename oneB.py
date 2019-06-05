#创建数据库

import sqlite3

conn=sqlite3.connect('test.db')

#创建表
print('Opened database successfully')
c=conn.cursor()
c.execute('''CREATE TABLE company
        (company INT PRIMARY KEY   NOT NULL,
         COUNT         INT   NOT NULL,
         WEIGHT        INT   NOT NULL,
         PRICE         INT   NOT NULL);''')
print('Table created successfully')
conn.commit()
conn.close()
#插入数据
conn=sqlite3.connect('test.db')
c=conn.cursor()
print ("Opened database successfully")
c.execute("INSERT INTO company(company,COUNT,WEIGHT,PRICE)  VALUES('张三粮配',2,32,64)");
c.execute("INSERT INTO company(company,COUNT,WEIGHT,PRICE)  VALUES('李四粮食',3,45,135)");
c.execute("INSERT INTO company(company,COUNT,WEIGHT,PRICE)  VALUES('王五小麦',2,44,88)");
c.execute("INSERT INTO company(company,COUNT,WEIGHT,PRICE)  VALUES('赵六麦子专营',2,55,110)");
conn.commit()
print('Records created successfully')
conn.close()
