#11725
import sys
from collections import deque

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n = int(input())  # 'node' 대신 'n'으로 변경
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
parent[1] = -1  # root

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    for neighbor in graph[v]:
        if parent[neighbor] == 0:
            parent[neighbor] = v
            dfs(neighbor)

dfs(1)

for i in range(2, n+1):
    print(parent[i])