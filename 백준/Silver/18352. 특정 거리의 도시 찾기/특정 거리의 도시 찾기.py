#18352
import sys
from collections import deque
    
def input():
    return sys.stdin.readline().rstrip()

# n:도시 수, m:도로 수, k:거리 정보, x:출발 도시
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    
distance = [-1] * (n+1)
distance[x] = 0

queue = deque([x])

while queue:
    current = queue.popleft()
    
    for neighbor in graph[current]:
        if distance[neighbor] == -1: # 노방문이라면
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)
            
result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)
        
if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)