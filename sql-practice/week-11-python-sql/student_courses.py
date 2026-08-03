# Week 11: list the courses and scores for one student.
import sqlite3
from pathlib import Path
database_path = Path(__file__).parent.parent / "week-10-database-design" / "university.db"
connection = sqlite3.connect(database_path)
print("Database connected")
cursor = connection.cursor()
print("Cursor ready")
while True:
    try:
        student_id = int(input("Enter a student ID: "))
        break
    except ValueError:
        print("Please enter a whole-number student ID.")

cursor.execute(
    """
    SELECT courses.course_name, enrolments.score
    FROM enrolments
    JOIN courses
    ON enrolments.course_code = courses.course_code
    WHERE enrolments.student_id = ?
    ORDER BY enrolments.course_code
    """,
    (student_id,),
)
print("Course query sent")
course_rows = cursor.fetchall()
print(course_rows)
if not course_rows:
    print("No courses found for this student.")
else:
    for course_row in course_rows:
        course_name = course_row[0]
        score = course_row[1]

        if score is None:
            print(f"{course_name}: Not graded")
        else:
            print(f"{course_name}: {score}")
connection.close()
print("Database closed")