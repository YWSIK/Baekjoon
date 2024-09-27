#18511
import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
sett = list(map(int, input().split()))

def recursive(current, sett, n):
    if int(current) > n:
        return -1
    
    max_val = int(current)
    
    for element in sett:
        next = current + str(element)
        max_val = max(max_val, recursive(next, sett, n))
    
    return max_val

result = recursive("0", sett, n)
print(result)