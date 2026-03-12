#1676
import sys
input = sys.stdin.readline

n = int(input())

count = 0
while n >= 5:
    n //= 5
    count += n

print(count)