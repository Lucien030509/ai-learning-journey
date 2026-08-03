# Week 11: enrol one fictional student in an existing course.
import sqlite3
from pathlib import Path

database_path = Path(__file__).parent.parent / "week-10-database-design" / "university.db"
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

new_student_id = 4
new_course_code = "INFO5990"
new_score = None

try:
    cursor.execute(
        "INSERT INTO enrolments (student_id, course_code, score) VALUES (?, ?, ?)",
        (new_student_id, new_course_code, new_score),
    )
    connection.commit()
    print("Student enrolled")
except sqlite3.IntegrityError:
    print("Student already enrolled in this course.")
connection.close()
print("Database connection closed.")
