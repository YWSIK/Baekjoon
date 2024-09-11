#1758
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    tip = 0
    tips = 0
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
        
    numbers.sort(reverse=True)
    
    i = 1
    while i <= n:
        tip += numbers[i-1] - (i-1)
        if tip < 0:
            tip = 0
        tips += tip
        tip = 0
        i += 1
        
    print(tips)
    
solve()