#10814
import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    [x, y] = sys.stdin.readline().split()
    arr.append([int(x), y])
    
arr.sort(key=lambda a: (a[0]))
for a in arr:
    print(a[0], a[1])