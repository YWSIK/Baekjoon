import sys
input = sys.stdin.readline

N = int(input())
edge = [list(map(int, input().split())) for _ in range(N)]

# 첫 번째 전봇대 기준 오름차순 정렬
edge = sorted(edge, key = lambda x: x[0])

# LIS
LIS = [1]*N

for idx in range(1, N):
    for i in range(idx):
        if edge[i][1] < edge[idx][1]:
            LIS[idx] = max(LIS[idx], LIS[i] + 1)

print(N - max(LIS))