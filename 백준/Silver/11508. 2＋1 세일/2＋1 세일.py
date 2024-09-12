#11508
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    milks = [int(input()) for _ in range(n)]
    milks.sort(reverse=True)
    result = 0
    cnt = 1
    
    for i in milks:
        result += i
        
        if cnt % 3 == 0:
            result -= i
        cnt += 1
            
    print(result)
    
solve()