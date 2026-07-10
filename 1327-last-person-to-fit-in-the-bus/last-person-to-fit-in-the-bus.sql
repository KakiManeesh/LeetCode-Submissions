#select person_name , weight , turn , sum(weight)  over (order by turn)
#from Queue

select person_name
from (
    select person_name , weight , turn , sum(weight)  over (order by turn) as  something
    from Queue
) as new_table
where something <= 1000
order by turn desc
limit 1