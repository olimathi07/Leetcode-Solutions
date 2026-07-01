(select u.name as results from users u
join movierating m on u.user_id=m.user_id
group by u.name,m.user_id
order by u.name asc,count(*) desc
limit 1)
union all
(
    select t.title from movies t join movierating m
    on t.movie_id=m.movie_id
    where m.created_at between '2020-02-01' and '2020-02-29'
    group by m.movie_id,t.title
    order by avg(rating)desc,t.title asc
    limit 1
)