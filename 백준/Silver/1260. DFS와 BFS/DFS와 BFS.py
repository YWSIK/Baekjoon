#1260
import sys
from collections import deque
    
def input():
    return sys.stdin.readline().rstrip()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
    
def bfs(graph, v, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

node, edge, start = map(int, input().split())
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs
visited = [False] * (node + 1)
dfs(graph, start, visited)
print()

# bfs
visited = [False] * (node + 1)
bfs(graph, start, visited)