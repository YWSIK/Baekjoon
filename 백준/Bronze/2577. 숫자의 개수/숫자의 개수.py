#2577
from collections import Counter

numbers = [int(input()) for _ in range(3)]
result = numbers[0] * numbers[1] * numbers[2]

cnt = Counter(str(result))

for i in range(10):
    print(cnt.get(str(i), 0))