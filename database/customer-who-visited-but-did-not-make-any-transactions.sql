# Write your MySQL query statement below
select customer_id, count(customer_id) as count_no_trans
from Transactions t
right join Visits v on t.visit_id=v.visit_id
where transaction_id is null
Group by customer_id;