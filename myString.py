student=[]
def addstudent():
    id=input("Enter an ID:")
    name=input("Enter a name:")
    dept=input("Enter department:")
    d={"id":id,"name":name,"dept":dept}
    student.append(d)
def viewstudent():
    for S in student:
        
            print("Student Name:{}, Student Id:{}, Student Dept:{}".format(S["name"],S["id"],S["dept"]))
def searchstudent(id):
    for S in student:
        if (S[id]==id):
            print("Student Name:{}, Student Id:{}, Student Dept:{}".format(S[name],S[id],S[dept]))
            break
    else: print("Student Not Found")
while(True):
    print("welcome to student infromation system (SIS)")
    print("1.Add Student:")
    print("2.View Student:")
    print("3.Search Student:")
    print("4.Delete Student:")
    print("5.Exit")
    choice=int(input("Enter Your Choice:"))
    match(choice):
        case 1:
            addstudent()
        case 2:
            viewstudent()
        case 3:
            searchstudent()
        case 4:
            deletestudent()
        case 5:
            exit("Bye")
            break
        case _:
            print("Invalid Choice")
