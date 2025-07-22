# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee e
INNER JOIN Employee em ON e.managerId = em.id
WHERE e.salary > em.salary