
select name as NAME,sum(t.amount) as BALANCE  from transactions t left join users u  on u.account=t.account  group by u.name,t.account having sum(t.amount)>10000;