import json
try:
   with open("students.json", "r")as file:
      students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
   students = []


while True:

    print("Student Grade Management")
    print("------------------------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. EXit")

    choice = input("Enter Your Choice: ")
    if choice not in["1","2","3","4","5","6"]:
       print("Invalid choice. Please try again.")
       continue

    if choice =="1":
        name = input("Enter Student name: ")
        grade = input("Enter Student grade: ")
        students.append([name, grade])
        with open("students.json", "w") as file:
           json.dump(students, file)
        print("Student added successfully!")
    if choice =="2":
        if students:
          for student in students:
            print("Name:", student[0],"|Grade:", student[1])
        else:
            print("No Students added yet")
    if choice =="3":
       name = input("Enter student name to search: ")
       found = False
       for student in students:
          if student[0] == name:
             print("Name:", student[0],"|grade: ", student[1])
             found = True
       if not found:
          print("Student not found") 

    if choice =="4":
       name = input("Enter student name to update: ")
       found = False
       for student in students:
          if student[0] == name:
             new_grade = input("Enter new grade: ")
             student[1] = new_grade
             found = True
             with open("student.json", "w")as file:
                json.dump(students, file)
             print("Grade updated successfully")
       if not found:
          print("Student not found")

    if choice =="5":
        name = input("Enter student name to delete: ")
        found = False
        for student in students:
              if student[0] == name:
                 students.remove(student)
                 found = True
                 with open("student.json", "w")as file:
                    json.dump(students, file)
                 print("Student deleted successfully")
        if not found:
              print("Student not found")
       
                     

    if choice =="6":
       print("Goodbye!")
       break

