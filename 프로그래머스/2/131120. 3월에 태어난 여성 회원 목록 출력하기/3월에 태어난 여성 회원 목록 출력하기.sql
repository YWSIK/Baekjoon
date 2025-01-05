SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth, '%Y-%m-%d')
FROM member_profile
WHERE gender = 'W' 
    AND tlno IS NOT null 
    AND date_of_birth LIKE '%-03-%'
ORDER BY member_id asc