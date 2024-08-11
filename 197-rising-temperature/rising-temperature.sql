# Write your MySQL query statement below
select id
from  Weather 
where temperature > (
    select temperature
    from Weather as w
    where w.recordDate = date_sub(Weather.recordDate,interval 1 day)
);