import mysql.connector
import csv

conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",   
    database="your_database"          
)

cursor = conn.cursor()
cursor.execute("create table if not exists student(id int primary key, name varchar(50), maths int,science int,social int,average float,result varchar(10))")

while True:
    print("OPERATIONS: \n1.INSERT STUDENT INFO \n2.RESULT \n3.AVERAGE \n4.MARKS \n5.DELETE \n6.VIEW ALL \n7.UPDATE \n8.EXPORT \n9.EXIT")
    inp = int(input("SELECT OPERATION: "))
    if inp == 1:
        num = int(input("ENTER NO OF STUDENTS: "))
        for i in range(num):
            id = int(input("ENTER ID: "))
            name = input("ENTER NAME: ")
            math = int(input("ENTER MATHS MARKS: "))
            sci = int(input("ENTER SCIENCE MARKS: "))
            soc = int(input("ENTER SOCIAL MARKS: "))
            avg = (math + sci + soc) / 3
            res = "PASS"
            if math < 35 or sci < 35 or soc < 35:
                res = "FAIL"
            cursor.execute('INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s)', (id, name, math, sci, soc, avg, res))
    if inp == 2:
        name = input("ENTER STUDENT FULL NAME : ")
        cursor.execute("select CONCAT('RESULT :',result) AS RESULT from student where name = %s",(name,))
        for i in cursor.fetchall():
            print(i[0])
    if inp == 3:
        name = input("ENTER STUDENT FULL NAME: ")
        cursor.execute("select concat('AVERAGE :',average) AS AVERAGE from student where name = %s",(name,))
        for i in cursor.fetchall():
            print(i[0])
    if inp == 4:
        name = input("ENTER STUDENT FULL NAME: ")
        cursor.execute("select CONCAT('MATHS:',maths,' ','SCIENCE:',science,' ','SOCIAL: ',social) AS MARKS from student where name = %s",(name,))
        for i in cursor.fetchall():
            print(i[0])
    if inp == 5:
        id = int(input(("ENTER ID TO DELETE: ")))
        cursor.execute("delete from student where id = %s",(id,))
        print("ID",id,"DELETED")
    if inp == 6:
        cursor.execute("select * from student")
        for i in cursor.fetchall():
            print(i)
    if inp == 7:
        print("WHAT TO CHANGE :\n1.ID \n2.NAME \n3.MATHS \n4.SCIENCE \n5.SOCIAL")
        opr = {1:'id',2:'name',3:'maths',4:'science',5:'social'}
        inp = int(input('OPERATION NUM: '))
        id = int(input("ENTER ID: "))
        change = input("ENTER NEW DATA: ")
        if inp in (1,3,4,5):
            change = int(change)
        if inp in (1,2,3,4,5):
            print((opr[inp],change,id))
            query = f"update student set {opr[inp]} = %s where id = %s"
            cursor.execute(query,(change,id))
            if inp in (3,4,5):
                cursor.execute("select maths,science,social from student where id = %s",(id,))
                val =  cursor.fetchall()[0]
                result = "Pass"
                print(val)
                avg = sum(val)/3
                if val[0] <35 or val[1]<35 or val[2] <35:
                    result = "Fail"
                query = f"update student set {opr[inp]} = %s,average = %s,result = %s where id = %s"
                cursor.execute(query,(change,avg,result,id))

    if inp == 8:
        cursor.execute("select * from student")
        data  = cursor.fetchall()
        with open('student.csv','w',newline='') as fobj:
            writer = csv.writer(fobj)
            writer.writerow(['ID','NAME','MATHS','SCIENCE','SOCIAL','AVERAGE','RESULT'])
            writer.writerows(data)
        print("DISPLAYING EXPORTED FILE:")
        with open('student.csv') as fobj:
            reader = csv.reader(fobj)
            for i in reader:
                print(i)
    if inp not in (1,2,3,4,5,6,7,8) or inp == 9:
        break



conn.commit()
conn.close()
