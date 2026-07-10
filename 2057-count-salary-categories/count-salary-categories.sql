/*
select 
    case
        when income < 20000  then "Low Salary"
        when income > 50000  then "High Salary"
        else "Average Salary"
    end as category , count(*) as accounts_count

from Accounts

group by category
*/
SELECT "Low Salary" AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000

union

SELECT "Average Salary" AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income >= 20000 and income <= 50000

union

SELECT "High Salary" AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000