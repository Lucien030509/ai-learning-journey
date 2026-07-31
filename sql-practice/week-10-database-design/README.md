# Week 10: Database Design

Goal: design a small university database before querying it.

## Data model

```text
students  1 ──< enrolments >── 1  courses
```

One `enrolments` row means one student has selected one course. It solves the many-to-many relationship between students and courses.

## Design choices verified

- `students.student_id` and `courses.course_code` are primary keys.
- `enrolments.student_id` and `enrolments.course_code` are foreign keys.
- `(student_id, course_code)` is a composite primary key, so duplicate enrolment is rejected.
- `NOT NULL` prevents an enrolment without a student or course.
- `CHECK (score BETWEEN 0 AND 100)` rejects impossible scores while still allowing an ungraded `NULL` score.
- Storing each course name once in `courses` avoids duplicated and inconsistent data. This is normalisation.

## Files

- `schema.sql`: the three-table database design
- `seed_data.sql`: fictional, repeat-safe sample data
- `university.db`: the local practice database
- `view_data.sql`: table views and the join query written during practice
- `run.sh`: runs the correct Week 10 viewer through VS Code

## Run in VS Code

Open a Week 10 `.sql` file and press `Command + Shift + B` (`⌘⇧B`). The lower terminal displays the data and query results.
