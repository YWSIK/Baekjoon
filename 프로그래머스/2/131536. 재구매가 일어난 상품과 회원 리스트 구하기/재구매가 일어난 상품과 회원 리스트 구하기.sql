SELECT O.user_id, O.product_id
FROM online_sale O
JOIN online_sale S
    ON O.user_id = S.user_id
    AND O.product_id = S.product_id
    AND O.sales_date < S.sales_date
GROUP BY O.user_id, O.product_id
ORDER BY O.user_id ASC, O.product_id DESC;