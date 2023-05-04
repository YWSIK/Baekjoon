#11650
import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort()
for a in arr:
    print(a[0], a[1])