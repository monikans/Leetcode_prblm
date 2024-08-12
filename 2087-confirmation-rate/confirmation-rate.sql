# Write your MySQL query statement below
SELECT 
    s.user_id, 
    ROUND(
        AVG(IF(c.action = 'confirmed', 1, 0)),2
    ) AS confirmation_rate
FROM 
    signups as s
LEFT JOIN 
    confirmations  as c
ON 
    s.user_id = c.user_id
GROUP BY 
    s.user_id;