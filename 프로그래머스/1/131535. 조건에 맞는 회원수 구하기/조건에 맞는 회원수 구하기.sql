SELECT count(*) as USERS
FROM user_info
WHERE year(joined) = 2021
AND age between 20 and 29;