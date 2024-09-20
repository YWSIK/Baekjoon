#16953
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    # 40021 -> 4002 -> 2001 -> 200 -> 100
    # 162 -> 81 -> 8 -> 4 -> 2
    # 42 -> 21 -> 2
    
    n, k = map(int, input().split())
    cnt = 0
    
    while n < k:
        if k % 2 == 0:
            k //= 2
        elif k % 10 == 1:
            k //= 10
        else:
            print(-1)
            return
        cnt += 1
    
    if k == n:
        print(cnt + 1)
    else:
        print(-1)
    
solve()