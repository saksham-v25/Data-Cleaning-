import os

FILE_NAME = "students.txt"

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{roll},{marks}\n")
    
    print("Student added successfully.\n")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as f:
        data = f.readlines()
        for line in data:
            name, roll, marks = line.strip().split(",")
            print(f"Name: {name}, Roll: {roll}, Marks: {marks}")
    print()

def search_student():
    roll_search = input("Enter Roll No to search: ")
    found = False

    with open(FILE_NAME, "r") as f:
        for line in f:
            name, roll, marks = line.strip().split(",")
            if roll == roll_search:
                print(f"Found -> Name: {name}, Marks: {marks}\n")
                found = True
                break
    
    if not found:
        print("Student not found.\n")

def delete_student():
    roll_delete = input("Enter Roll No to delete: ")
    lines = []

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    with open(FILE_NAME, "w") as f:
        for line in lines:
            name, roll, marks = line.strip().split(",")
            if roll != roll_delete:
                f.write(line)

    print("Record deleted if existed.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice\n")
