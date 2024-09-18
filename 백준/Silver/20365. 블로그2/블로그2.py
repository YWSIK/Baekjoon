#20365
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    blocks = input()
    
    blue_cnt = 0
    red_cnt = 0
    
    if blocks[0] == 'B':
        blue_cnt += 1
    else:
        red_cnt += 1
        
    for i in range(1, n):
        if blocks[i] != blocks[i-1]:
            if blocks[i] == 'B':
                blue_cnt += 1
            else:
                red_cnt += 1
                
    print(min(blue_cnt, red_cnt) + 1)
    
solve()