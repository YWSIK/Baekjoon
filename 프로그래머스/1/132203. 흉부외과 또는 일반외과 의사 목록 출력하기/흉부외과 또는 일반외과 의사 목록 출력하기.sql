SELECT dr_name, dr_id, mcdp_cd, DATE_FORMAT(hire_ymd, '%Y-%m-%d')
FROM doctor
WHERE mcdp_cd = 'GS' or mcdp_cd = 'CS'
ORDER BY hire_ymd desc, dr_name asc