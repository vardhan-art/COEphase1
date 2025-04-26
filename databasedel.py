import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="vardhan",database="ACE")
c = conn.cursor()
sid=input("Enter your id to delete record from DB")
c.execute("Delete from students where sid=%s",(sid, ))
conn.commit()
c.close()
conn.close()



