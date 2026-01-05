#1764
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split(" "))
listen = []
see = []

for i in range(n):
    listen.append(input())

for i in range(n, n+m):
    see.append(input())
 
lis_see = sorted(list(set(listen) & set(see)))

print(len(lis_see))
for i in lis_see:
    print(i)