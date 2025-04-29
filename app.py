from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector
from db import get_connection

app = Flask(__name__)


# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Pages to add data
@app.route('/student_form')
def student_form():
    return render_template('add_student.html')

@app.route('/course_form')
def course_form():
    return render_template('add_course.html')

@app.route('/enroll_form')
def enroll_form():
    return render_template('enroll_student.html')

# APIs
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(students)

@app.route('/courses', methods=['GET'])
def get_courses():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Course")
    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(courses)

@app.route('/enrollments', methods=['GET'])
def get_enrollments():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT e.EnrollmentID, s.Name AS StudentName, c.Title AS CourseTitle
        FROM Enrollment e
        JOIN Student s ON e.StudentID = s.StudentID
        JOIN Course c ON e.CourseID = c.CourseID
    """)
    enrollments = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(enrollments)

# Submit student from form
@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Student (Name, Email, Password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('home'))

# Submit course from form
@app.route('/add_course', methods=['POST'])
def add_course():
    title = request.form['title']
    description = request.form['description']
    schedule_time = request.form['schedule_time']
    capacity = request.form['capacity']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Course (Title, Description, ScheduleTime, Capacity) VALUES (%s, %s, %s, %s)",
        (title, description, schedule_time, capacity)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('home'))

# Submit enrollment from form
@app.route('/enroll', methods=['POST'])
def enroll_student():
    student_id = request.form['student_id']
    course_id = request.form['course_id']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Enrollment (StudentID, CourseID) VALUES (%s, %s)",
        (student_id, course_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
