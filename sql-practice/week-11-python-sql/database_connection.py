# Week 11: query the Week 10 SQLite database from Python.
import sqlite3
print(sqlite3.sqlite_version)
from pathlib import Path
database_path = Path(__file__).parent.parent / "week-10-database-design" / "university.db"
print(database_path.exists())
connection = sqlite3.connect(database_path)
print("Database connected")
cursor = connection.cursor()
print("cursor ready")
while True:
    try:
        student_id = int(input("Enter a student ID:"))
        break
    except ValueError:
        print("Please enter a whole-number student ID.")
cursor.execute(
    "SELECT student_id, name FROM students WHERE student_id = ?",
    (student_id,),
)
print("Query sent")
student = cursor.fetchone()
print(student)
if student is None:
    print("Student not found")
else:
    print(f"{student[0]}: {student[1]}")
connection.close()
print("Database closed")