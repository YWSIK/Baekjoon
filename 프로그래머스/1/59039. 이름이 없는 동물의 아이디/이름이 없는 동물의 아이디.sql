# 이름이 없는 채로 들어온 동물 id, 오름차순 정렬

select animal_id
  from animal_ins
 where name is null
 order by name desc;