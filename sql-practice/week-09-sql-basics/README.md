# Week 9: SQL Basics

Goal: ask clear questions of data stored in related tables.

## Practice database

`learning.db` is a local SQLite database. It contains two tables:

| Table | Purpose | Important columns |
| --- | --- | --- |
| `students` | one row per student result | `name`, `course`, `score` |
| `courses` | one row per course | `code`, `course_name` |

`students.course` and `courses.code` both store a course code such as `COMP9001`. They are the matching values used by a join.

## Skills verified

- Read table data with `SELECT ... FROM ...`.
- Filter original rows with `WHERE`.
- Sort results with `ORDER BY ... DESC`.
- Calculate `AVG()` and `COUNT(*)` after `GROUP BY`.
- Filter grouped results with `HAVING`.
- Combine related tables with `JOIN ... ON ...`.
- Keep all rows from the left table with `LEFT JOIN`.

## Files

- `learning.db`: local SQLite practice database
- `queries.sql`: SQL written during the exercises
- `run_queries.sh`: terminal fallback for running the whole SQL file

## Run a query in VS Code

1. Open `queries.sql` and save it.
2. Confirm the VS Code status bar shows `SQLite: learning.db`.
3. Press `Option + Command + R` (`⌥⌘R`).

The SQLite results view shows the resulting table.
