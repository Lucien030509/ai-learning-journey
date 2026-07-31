-- A read-only view of the Week 10 sample database.

SELECT * FROM students ORDER BY student_id;

SELECT * FROM courses ORDER BY course_code;

SELECT * FROM enrolments ORDER BY student_id, course_code;
SELECT * FROM enrolments
WHERE student_id = 1;
SELECT courses.course_name, COALESCE(enrolments.score, 'Not graded') AS score_status
FROM enrolments
JOIN courses
ON enrolments.course_code = courses.course_code
WHERE enrolments.student_id = 1;