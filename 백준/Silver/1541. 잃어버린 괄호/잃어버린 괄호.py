#1541
# (+, -) 뿐인 연산
# 숫자를 크기순으로 나열
sik = input()
parts = sik.split('-')

result = sum(map(int, parts[0].split('+'))) #첫번째 숫자는 +

#-로 나눠진 애들 더하고 마지막에 뺌
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))
    
    
print(result)