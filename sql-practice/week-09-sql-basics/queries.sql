SELECT * FROM students 
WHERE course = 'COMP9001';
SELECT course, AVG(score) AS average_score, COUNT(*) AS student_count
FROM students
GROUP BY course
HAVING AVG(score) >=  80  
ORDER BY average_score DESC;
SELECT * FROM courses;
SELECT students.name, courses.course_name, students.score
FROM students
JOIN courses
ON students.course = courses.code
WHERE students.score >= 80
ORDER BY students.score DESC;
SELECT courses.course_name, students.name
FROM courses
LEFT JOIN students
ON courses.code = students.course;