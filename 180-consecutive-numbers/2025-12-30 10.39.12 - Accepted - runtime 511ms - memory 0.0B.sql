select distinct num as ConsecutiveNums from
(
select num,lag(num,1) over(order by id) as p1,
lag(num,2) over (order by id) as p2
from logs
) t
where num=p1 and p1=p2;