#1149
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

costs = []

for _ in range(n):
    r, g, b = map(int, input().split())
    costs.append([r, g, b])
    
dp = [[0] * 3 for _ in range(n)]

dp[0][0] = costs[0][0] #첫번째 집 R로 칠하기
dp[0][1] = costs[0][1] #첫번째 집 G로 칠하기
dp[0][2] = costs[0][2] #첫번째 집 B로 칠하기

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0] #i번째 집 R로
    dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + costs[i][1] #i번째 집 G로
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2] #i번째 집 B로
    
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))