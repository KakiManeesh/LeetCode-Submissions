select distinct num as consecutiveNums
from  Logs as l1

where l1.num =(select l2.num from Logs as l2 where l2.id = l1.id+1 ) and l1.num =(select l3.num from Logs as l3 where l3.id = l1.id+2 )