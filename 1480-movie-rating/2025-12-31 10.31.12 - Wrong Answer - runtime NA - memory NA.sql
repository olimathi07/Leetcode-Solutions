(select u.name as results from movierating m
join users u on m.user_id=u.user_id
group by u.name,m.user_id
order by u.name asc,count(*) desc
limit 1)
union all
(
    select t.title as results from movierating m join movies t
    on m.movie_id=t.movie_id
    where m.created_at between '2020-02-01' and '2020-02-29'
    group by m.movie_id,t.title
    order by avg(m.rating)desc,t.title asc
    limit 1
)