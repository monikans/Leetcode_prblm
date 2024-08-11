# Write your MySQL query statement below
select product_name,year,price
from sales as s
Left join Product as p
on p.product_id = s.product_id;