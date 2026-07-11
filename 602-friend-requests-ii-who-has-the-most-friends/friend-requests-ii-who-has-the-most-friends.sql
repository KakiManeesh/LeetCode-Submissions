select f1 as id , count(*) as num
from (
    select requester_id as f1 , accepter_id as f2 from RequestAccepted 
    union 
    select accepter_id as f1 , requester_id as f2 from RequestAccepted 
) as new_table
group  by f1
order by count(*) desc
limit 1