# 2295
import sys

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

sum_set = set()

for i in range(n):
    for j in range(i, n):
        sum_set.add(numbers[i] + numbers[j])
        
# 큰 수부터 확인
for k in range(n-1, -1, -1):
    for c in range(k):
        if numbers[k] - numbers[c] in sum_set:
            print(numbers[k])
            sys.exit()
