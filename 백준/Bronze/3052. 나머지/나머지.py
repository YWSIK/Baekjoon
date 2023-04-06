#3052
# 10개 입력, 42로 나눔. 서로 다른 나머지가 몇 개인지
num = []

for i in range(10):
    n = int(input())
    
    if n % 42 not in num:
        num.append(n % 42)
print(len(num))