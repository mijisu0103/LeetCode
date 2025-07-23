# Write your MySQL query statement below
SELECT s.user_id, CASE WHEN c.action is null THEN 0 else round(sum(c.action="confirmed")/count(*),2) end AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
USING (user_id)
GROUP BY s.user_id