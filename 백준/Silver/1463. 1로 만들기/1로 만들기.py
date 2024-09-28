#1463
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
cnt = 0
dp = [0] * (n+1)

dp[1] = 0
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # case -1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) # case /2
        
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) # case /3
        
print(dp[n])

'''
-1 : dp[i] = dp[i-1] + 1
/3 : dp[i] = dp[i/3] + 1
/2 : dp[i] = dp[i/2] + 1
'''