import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

for _ in range(m):
    start, end = map(int, input().split())
    print(prefix[end] - prefix[start - 1])
