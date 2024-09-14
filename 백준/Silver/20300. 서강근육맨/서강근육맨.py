#20300
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    muscles = list(map(int, input().split()))
    muscles.sort()
    
    max_loss = 0
    
    if n % 2 == 1:
        max_loss = muscles[n-1]
        n -= 1
    
    for i in range(n//2):
        max_loss = max(max_loss, muscles[i] + muscles[n-i-1])
    
    print(max_loss)
    
solve()