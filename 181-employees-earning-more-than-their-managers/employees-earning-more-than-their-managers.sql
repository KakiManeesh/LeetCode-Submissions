# Write your MySQL query statement below


select name as Employee
from Employee as e
where e.managerId is not null and e.salary > (select e2.salary from Employee as e2 where e.managerId = e2.id); 