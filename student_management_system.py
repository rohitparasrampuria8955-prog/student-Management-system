import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohit@2004",
    database="student_datailes"
)
cursor=conn.cursor()


def add_student():
    name=input("Enter student name: ")
    age=int(input("Enter student age: "))
    course_name=input("Enter course name: ")
    marks=int(input("Enter student marks: "))

    query = "insert into student(student_name,age,course_name,marks)values(%s,%s,%s,%s)"
    values = (name,age,course_name,marks)
    cursor.execute(query, (values))
    conn.commit()
    print(" Student Added Successfully")


def view_student_details():
    name=input('Enter student name')
    query = "select * from student where student_name = %s"
    cursor.execute(query,(name,))

    data = cursor.fetchall()

    if data:
        print("search name in data")
        for row in data:
            print(row)
        else:
            print("no student found")

def view_all_student_details():
    query="select * from student"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print(row)

def update_student_details():
    id=int(input("Enter student id"))
    marks = int(input("Enter student marks"))

    query="update student set marks=%s where s_id=%s"
    cursor.execute(query,(marks,id))
    conn.commit()
    print("student deatail update successfully")

def delete_student():
    id=int(input("Enter student id"))

    query="delete from student where s_id = %s"
    cursor.execute(query,(id,))
    conn.commit()
    print("remove student successfully")


while True:
    print("\n  3studnet management system")
    print("1.add_student")
    print("2.view_student_details")
    print("3.view_all_student_details")
    print("4.update_student_details")
    print("5.delete_student")
    print("6.exit")

    num=int(input("Enter your operation no"))

    if num==1:
        add_student()
    elif num==2:
        view_student_details()
    elif num==3:
        view_all_student_details()
    elif num==4:
        update_student_details()
    elif num==5:
        delete_student()
    elif num==6:
        print("exiting")
        break
    else:
        print("invalid choice")

# git add.student_management_system.py
# git commit -m "first commit"
# git push -u origin main

