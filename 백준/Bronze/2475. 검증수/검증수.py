#2475
import sys
def input():
    return sys.stdin.readline().rstrip()
sum = 0
numbers = list(map(int, input().split(" ")))

for num in numbers:
    sum += num ** 2

print(sum % 10)