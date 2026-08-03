# Week 11: Python and SQLite

This week connects Python programs to the normalized SQLite university database
created in Week 10.

## Completed practice

- `database_connection.py`: connects to the database, validates an integer
  student ID, uses a parameterised `SELECT`, and handles a missing student.
- `student_courses.py`: uses a SQL `JOIN`, reads multiple rows with
  `fetchall()`, and displays a missing score as `Not graded`.
- `add_student.py`: adds a fictional student with `INSERT` and `commit()`,
  while safely handling a duplicate primary key.
- `enrol_student.py`: adds an enrolment with a `NULL` score and safely handles
  a duplicate `(student_id, course_code)` pair.
- `run.sh`: runs `database_connection.py` from this folder.

## Key ideas

- A `connection` opens the route from Python to the SQLite database.
- A `cursor` sends SQL and receives query results.
- `?` placeholders keep SQL values separate from the SQL instruction.
- `fetchone()` returns one row, or `None` when no row exists.
- `fetchall()` returns a list of all matching rows.
- `commit()` permanently saves an `INSERT` change.
- `sqlite3.IntegrityError` lets the program handle database-rule violations
  without crashing.

## Verified examples

- Student ID `4` returns Zoe.
- Student ID `99` returns `Student not found`.
- Zoe's `INFO5990` enrolment displays as `Not graded` because its score is
  `NULL` in SQLite.
- Re-running the same enrolment shows a friendly duplicate-enrolment message.
