# Week 7: Data Cleaning

This exercise cleans a small student-score dataset with Pandas.

## Files

- `messy_students.csv`: intentionally messy source data
- `clean_student_data.py`: reads, cleans, and saves the data
- `clean_students.csv`: cleaned output data

## Cleaning rules used

1. Convert `score` to numeric values. Invalid text becomes a missing value (`NaN`).
2. Remove exact duplicate records.
3. Remove records with a missing score, because this exercise has no reliable value to use instead.
4. Reset row indexes and save the cleaned result without indexes.

## Result

The source dataset has 6 rows. The cleaned dataset has 3 complete and unique student records.
