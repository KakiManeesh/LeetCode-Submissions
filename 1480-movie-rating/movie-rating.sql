(
sElect name as results
from MovieRating
join Users Using(user_id)
group by user_id
order by count(*) Desc ,name
limit 1
)
union all 

(
select title as  results
from MovieRating
join Movies Using(movie_id)
WHERE created_at >= '2020-02-01' AND created_at < '2020-03-01'
group by movie_id 
order by  avg(rating) desc ,  title
limit 1
)