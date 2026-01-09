# 동물 중 이름이 있는 동물의 id, id 오름차순
select animal_id
  from animal_ins
 where name is not null
 order by 1;