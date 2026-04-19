# Write your MySQL query statement below
select EmployeeUNI.unique_id , name
from Employees
Left Join EmployeeUNI
on Employees.id = EmployeeUNI.id;
