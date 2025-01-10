SELECT id, length
FROM fish_info
WHERE length > 10
ORDER BY length desc, id asc
LIMIT 10;