import sys
from collections import deque

def josephus(queue, k):
    result = []
    while queue:
        queue.rotate(-k+1)
        result.append(str(queue.popleft()))
    return result

n, k = map(int, sys.stdin.readline().split())
queue = deque(range(1, n+1))

if n == 1:
    result = [str(queue[0])]
else:
    result = josephus(queue, k)

print("<" + ", ".join(result) + ">")
