# Write your MySQL query statement below

select contest_id ,
    round( 100*count(r.user_id) / (select count(*) from Users) ,2 ) as percentage

from Register as r

group by contest_id

order by percentage desc , contest_id  ;