from db import get_connection

def create_course(title, description, schedule_time, capacity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Course (Title, Description, ScheduleTime, Capacity) VALUES (%s, %s, %s, %s)",
        (title, description, schedule_time, capacity)
    )
    conn.commit()
    conn.close()
    print("✅ Course created.")

def read_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Course")
    for course in cursor.fetchall():
        print(course)
    conn.close()

def update_course(course_id, title, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Course SET Title = %s, Description = %s WHERE CourseID = %s",
        (title, description, course_id)
    )
    conn.commit()
    conn.close()
    print("✅ Course updated.")

def delete_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Course WHERE CourseID = %s", (course_id,))
    conn.commit()
    conn.close()
    print("✅ Course deleted.")
