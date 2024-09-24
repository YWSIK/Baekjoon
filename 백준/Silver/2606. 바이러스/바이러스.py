#2606
import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    cnt = 1 # 자기자신
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            cnt += dfs(graph, neighbor, visited)
            
    return cnt
    
def input():
    return sys.stdin.readline().rstrip()

com = int(input()) # 컴퓨터 수
node = int(input()) # 간선 수
graph = [[] for _ in range(com+1)]

for _ in range(node):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (com+1)

infect = dfs(graph, 1, visited) - 1

print(infect)