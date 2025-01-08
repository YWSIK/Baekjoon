SELECT book_id, DATE_FORMAT(published_date, '%Y-%m-%d') as PUBLISHED_DATE
FROM book
WHERE published_date like '2021%'
AND category like '인문'
ORDER BY published_date asc