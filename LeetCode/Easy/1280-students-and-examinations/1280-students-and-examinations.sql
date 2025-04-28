# Write your MySQL query statement below
SELECT 
    s.student_id, 
    s.student_name,
    su.subject_name,
    COALESCE(
        (SELECT COUNT(1)
         FROM Examinations e
         WHERE e.student_id = s.student_id
         AND e.subject_name = su.subject_name), 
        0
    ) AS attended_exams
FROM Students s
CROSS JOIN Subjects su
ORDER BY s.student_id, su.subject_name;
