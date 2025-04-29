from course import *
from student import *
from enrollment import *

while True:
    print("\n--- Registration System ---")
    print("1. Manage Courses")
    print("2. Manage Students")
    print("3. Manage Enrollments")
    print("4. Exit")
    choice = input("Select option: ")

    if choice == "1":
        print("\n1. Create Course\n2. View Courses\n3. Update Course\n4. Delete Course")
        c_choice = input("Select option: ")
        if c_choice == "1":
            create_course(input("Title: "), input("Description: "), input("Schedule: "), int(input("Capacity: ")))
        elif c_choice == "2":
            read_courses()
        elif c_choice == "3":
            update_course(int(input("Course ID: ")), input("New Title: "), input("New Description: "))
        elif c_choice == "4":
            delete_course(int(input("Course ID: ")))

    elif choice == "2":
        print("\n1. Create Student\n2. View Students\n3. Update Student\n4. Delete Student")
        s_choice = input("Select option: ")
        if s_choice == "1":
            create_student(input("Name: "), input("Email: "), input("Password: "))
        elif s_choice == "2":
            read_students()
        elif s_choice == "3":
            update_student(int(input("Student ID: ")), input("New Name: "), input("New Email: "))
        elif s_choice == "4":
            delete_student(int(input("Student ID: ")))

    elif choice == "3":
        print("\n1. Enroll Student\n2. View Enrollments\n3. Delete Enrollment")
        e_choice = input("Select option: ")
        if e_choice == "1":
            enroll_student(int(input("Student ID: ")), int(input("Course ID: ")))
        elif e_choice == "2":
            read_enrollments()
        elif e_choice == "3":
            delete_enrollment(int(input("Enrollment ID: ")))

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option. Try again.")
