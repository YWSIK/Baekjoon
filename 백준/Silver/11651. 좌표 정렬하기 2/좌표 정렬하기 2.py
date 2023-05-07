import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    arr.append([x, y])
    
arr.sort(key=lambda a: (a[1], a[0]))
for a in arr:
    print(a[0], a[1])