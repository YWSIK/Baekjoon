SELECT warehouse_id, warehouse_name, address,IFNULL(freezer_yn, 'N') as FREEZER_YN
FROM food_warehouse
WHERE address like '경기도%'
ORDER BY warehouse_id asc