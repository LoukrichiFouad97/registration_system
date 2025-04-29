from db import get_connection

def enroll_student(student_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Enrollment (StudentID, CourseID) VALUES (%s, %s)",
        (student_id, course_id)
    )
    conn.commit()
    conn.close()
    print("✅ Student enrolled.")

def read_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT e.EnrollmentID, s.Name, c.Title FROM Enrollment e JOIN Student s ON e.StudentID = s.StudentID JOIN Course c ON e.CourseID = c.CourseID"
    )
    for enrollment in cursor.fetchall():
        print(enrollment)
    conn.close()

def delete_enrollment(enrollment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Enrollment WHERE EnrollmentID = %s", (enrollment_id,))
    conn.commit()
    conn.close()
    print("✅ Enrollment deleted.")
