# Week 10 Design Notes

The university practice database separates facts into three tables:

- `students`: one row per student.
- `courses`: one row per course.
- `enrolments`: one row per student-course relationship, including that student's score.

This structure allows a student to take many courses and a course to have many students without repeating course names in every enrolment row.

The schema protects data quality with primary keys, foreign keys, `NOT NULL`, and a score-range `CHECK` constraint.
