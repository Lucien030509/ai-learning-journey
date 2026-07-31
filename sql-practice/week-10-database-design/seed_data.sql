-- Fictional practice data. INSERT OR IGNORE keeps this file safe to run again.
PRAGMA foreign_keys = ON;

INSERT OR IGNORE INTO students (student_id, name) VALUES
    (1, 'Estella'),
    (2, 'Alex'),
    (3, 'Mia');

INSERT OR IGNORE INTO courses (course_code, course_name) VALUES
    ('COMP9001', 'Programming Fundamentals'),
    ('COMP9120', 'Database Management Systems'),
    ('COMP5310', 'Principles of Data Science'),
    ('INFO5990', 'Professional Practice in IT');

INSERT OR IGNORE INTO enrolments (student_id, course_code, score) VALUES
    (1, 'COMP9001', 85),
    (1, 'COMP9120', 90),
    (1, 'COMP5310', 78),
    (1, 'INFO5990', NULL),
    (2, 'COMP9001', 92),
    (2, 'COMP9120', 88),
    (3, 'COMP5310', 78);
