import mysql.connector


conn = mysql.connector.connect(
    host="mysql-12ad5647-loukrichi4-6ea2.l.aivencloud.com",
    user="avnadmin",         
    password="AVNS_Z_57T7rhtzNvEpcjRSD",     
    database="registration_system",
    port=22332
)

cursor = conn.cursor()

# CREATE Course
def create_course(title, description, schedule_time, capacity):
    cursor.execute(
        "INSERT INTO Course (Title, Description, ScheduleTime, Capacity) VALUES (%s, %s, %s, %s)",
        (title, description, schedule_time, capacity)
    )
    conn.commit()
    print("✅ Course created.\n")

# READ Courses
def read_courses():
    cursor.execute("SELECT * FROM Course")
    courses = cursor.fetchall()
    for course in courses:
        print(course)

# UPDATE Course
def update_course(course_id, new_title, new_description):
    cursor.execute(
        "UPDATE Course SET Title = %s, Description = %s WHERE CourseID = %s",
        (new_title, new_description, course_id)
    )
    conn.commit()
    print("✅ Course updated.\n")

# DELETE Course
def delete_course(course_id):
    cursor.execute("DELETE FROM Course WHERE CourseID = %s", (course_id,))
    conn.commit()
    print("✅ Course deleted.\n")

# Simple Menu
while True:
    print("\n1. Create Course\n2. View Courses\n3. Update Course\n4. Delete Course\n5. Exit")
    choice = input("Select option: ")

    if choice == "1":
        t = input("Title: ")
        d = input("Description: ")
        s = input("Schedule Time: ")
        c = int(input("Capacity: "))
        create_course(t, d, s, c)

    elif choice == "2":
        read_courses()

    elif choice == "3":
        cid = int(input("Course ID to update: "))
        new_t = input("New Title: ")
        new_d = input("New Description: ")
        update_course(cid, new_t, new_d)

    elif choice == "4":
        cid = int(input("Course ID to delete: "))
        delete_course(cid)

    elif choice == "5":
        break

    else:
        print("❌ Invalid option. Try again.")

cursor.close()
conn.close()