with cte as(
    select
  d.name as Department,
  e.name as Employee,
  e.salary as Salary, 
      dense_rank() over(partition by e.departmentid order by e.salary desc)  as 'rn'
  from employee e
  join department d
  on e.departmentid=d.id
)
select Department,Employee,Salary 
from cte where rn=1;