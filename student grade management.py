#initiating a dictionary
student_grades = { } 

#add a new student
def add_student(name,grade):
    student_grades[name]=grade
    print(f"Added {name} with grade {grade}")

#update a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"Updated {name} with grade {grade}")
    else:
        print(f"{name} was not found")

#delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Deleted {name} successfully")
    else:
        print(f"{name} was not found")

#view all students 
def view_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No student has been added yet")

#exit programme
def exit():
    print("Closing the programme...")



def main():
    while True:
        print('\n STUDENT GRADES MANAGEMENT SYSTEM \n')
        print('1. Add student')
        print('2. Update student')
        print('3. Delete student')
        print('4. View students')
        print('5. Exit')

        operation = int(input(f"Select operation you want to perform : "))

        #add
        if operation == 1 :
            name = input(f"Enter Name : ")
            grade = int(input(f"Enter Grade : "))
            add_student(name,grade)

        #update
        elif operation == 2 :
            name = input(f"Enter name you want to update : ")
            grade = int(input(f"Enter his/her new grade : "))
            update_student(name,grade)

        #delete
        elif operation == 3 :
            name = input(f"Enter name you want to delete : ")
            delete_student()

        #view    
        elif operation == 4 :
            view_student()

        #exit    
        elif operation == 5 :
            exit()
            break

        else:
            print("Invalid input")

#execute 
main()