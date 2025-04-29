from db import get_connection

def create_student(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Student (Name, Email, Password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    conn.commit()
    conn.close()
    print("✅ Student created.")

def read_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    for student in cursor.fetchall():
        print(student)
    conn.close()

def update_student(student_id, name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Student SET Name = %s, Email = %s WHERE StudentID = %s",
        (name, email, student_id)
    )
    conn.commit()
    conn.close()
    print("✅ Student updated.")

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Student WHERE StudentID = %s", (student_id,))
    conn.commit()
    conn.close()
    print("✅ Student deleted.")
