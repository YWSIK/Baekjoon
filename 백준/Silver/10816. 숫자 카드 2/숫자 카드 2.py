#10816
from collections import Counter

n = int(input())
arr1 = list(map(int, input().split(" ")))

m = int(input())
arr2 = list(map(int, input().split(" ")))

cnt = Counter(arr1)

result = [cnt[i] for i in arr2]
print(' '.join(map(str, result)))