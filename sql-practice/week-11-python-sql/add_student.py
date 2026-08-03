# Week 11: add one fictional student to the practice database.
import sqlite3
from pathlib import Path

database_path = Path(__file__).parent.parent / "week-10-database-design" / "university.db"
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

new_student_id = 4
new_student_name = "Zoe"

try:
    cursor.execute(
        "INSERT INTO students (student_id, name) VALUES (?, ?)",
        (new_student_id, new_student_name),
    )
    connection.commit()
    print("Student added")
except sqlite3.IntegrityError:
    print("Student already exists.")
connection.close()