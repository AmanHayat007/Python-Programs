import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
list1 = [('abc','add1',25,'23456'),
         ('abc','add2',24,'12345'),
         ('abc','add3',29,'98765'),]

c.executemany('INSERT INTO studentz VALUES(?,?,?,?)',list1)

for row in c.execute('SELECT * FROM studentz'):
    print (row)