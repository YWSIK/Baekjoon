#20115
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    result = 0
    drinks = list(map(int, input().split()))
    drinks.sort(reverse=True)
    
    result += drinks[0]
    
    for i in range(1, n):
        result += drinks[i] / 2
    
    print(result)

solve()