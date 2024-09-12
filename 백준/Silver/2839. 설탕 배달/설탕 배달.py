#2839
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    result = 0
    n = int(input())
    
    while n >= 0:
        if n % 5 == 0:
            result += (n // 5)
            print(result)
            return
        n -= 3
        result += 1
        
    print(-1)
    
solve() 