#13305
n = int(input())
km = list(map(int, input().split()))
liter = list(map(int, input().split()))

result = 0

#처음에는 무조건 주유
min_price = liter[0]

for i in range(n-1): #마지막엔 주유 안해도 됨
    #현재 가격이 저렴하면 뒤 거리 만큼 더 함
    if liter[i] <= min_price:
        min_price = liter[i]
    
    result += min_price * km[i]
    
print(result)