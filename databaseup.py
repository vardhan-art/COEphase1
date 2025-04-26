import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="vardhan",database="ACE")
c = conn.cursor()
sid=input("Enter your id to update record from DB")
marks=input("Enter your updated marks:")
c.execute("Update  students set marks=%s where sid=%s",(marks,sid ))
conn.commit()
c.close()
conn.close()



