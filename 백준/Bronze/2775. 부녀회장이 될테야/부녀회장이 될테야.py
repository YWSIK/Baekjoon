#2775
# 2층 3호 = 10 / 2층 2호 = 4
# 1층 3호 = 6 / 1층 2호 = 3 / 1층 1호 = 1
# 0층 3호 = 3, 0층 2호 = 2, 0층 1호 = 1

# people[k][n] = people[k-1][1] + people[k-1][2] + ... + people[k-1][n]
# people[k][n-1] + people[k-1][n]

import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    k = int(input().strip())
    n = int(input().strip())
    
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = i
        
    for floor in range(1, k+1):
        for i in range(1, n+1):
            dp[i] = dp[i] + dp[i-1]
            
    print(dp[n])