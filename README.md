# 📚 Student Registration System

A simple command-line and web-based registration system built with **Python**, **MySQL**, and **Flask**. This project allows admins to manage **Students**, **Courses**, and **Enrollments**, with both API endpoints and a minimal HTML interface.

---

## 🧠 1. Introduction

This system is designed to manage basic academic registration tasks:
- Add/update/delete Students
- Add/update/delete Courses
- Enroll students into Courses

Technologies used:
- Python 3
- MySQL (with online connection support)
- Flask (for web interface and API)

---

## 🎯 2. Work Goals and Tasks

- Design and implement a modular student registration system
- Perform CRUD operations on Students, Courses, Enrollments
- Use online MySQL as a backend
- Create API endpoints and a basic web interface using Flask

---

## 👤 3. System Actors

- **Admin/User**: Manages students, courses, and enrollments.
- **Student**: Enrolled in courses (via admin actions).
- **Course**: Entity representing an academic offering.

---

## ⚙️ 4. Functional Requirements

| Functionality         | Description                                           |
|-----------------------|-------------------------------------------------------|
| Manage Students        | Create, view, update, delete students                |
| Manage Courses         | Create, view, update, delete courses                 |
| Manage Enrollments     | Enroll students into courses, view and remove enrollments |
| Secure DB Connection   | Connect Python to online MySQL using credentials     |

---

### 📌 4.1 Use Case Diagram (Text-Based)



### 🔁 4.2 Basic & Alternative Scenarios

- **Basic Flow**:
  1. Run program or web app
  2. Choose to manage students/courses/enrollments
  3. Perform CRUD operations

- **Alternative Flow**:
  - Handle invalid input
  - Handle DB connection failure gracefully

---

## 🗃 5. Database Model

### 5.1 Entity Relationship (ER)

- **Student** `1---*` **Enrollment** `*---1` **Course**

### 5.2 Logical Model

| Table     | Fields                                      |
|-----------|---------------------------------------------|
| Student   | StudentID (PK), Name, Email, Password       |
| Course    | CourseID (PK), Title, Description, ScheduleTime, Capacity |
| Enrollment| EnrollmentID (PK), StudentID (FK), CourseID (FK) |

### 5.3 Physical Model

- DB Name: `registration_db`
- All tables created with proper types and foreign keys

---

## 🧾 6. SQL Examples

```sql
-- Add a student
INSERT INTO Student (Name, Email, Password)
VALUES ('John Doe', 'john@example.com', '1234');

-- View courses
SELECT * FROM Course;

-- Update course
UPDATE Course SET Title = 'Python Advanced' WHERE CourseID = 1;

-- Delete enrollment
DELETE FROM Enrollment WHERE EnrollmentID = 2;
