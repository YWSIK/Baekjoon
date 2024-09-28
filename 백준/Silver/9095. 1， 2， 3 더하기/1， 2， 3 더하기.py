#9095
import sys

def input():
    return sys.stdin.readline().rstrip()

dp = [0] * 11
n = int(input())

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
while n > 0:
    k = int(input())
    print(dp[k])
    n -= 1
    
'''
n=1 , 1
n=2 , 1,1 / 2 => 2
n=3 , 1,1,1 / 1,2 / 2,1 / 3 => 4
n=4 , 1,1,1,1 / 1,1,2 / 1,2,1 / 2,1,1 / 2,2 / 3,1 / 1,3 = 7
n=5 , 1,1,1,1,1 / 1,1,1,2 / 1,1,2,1 / 1,2,1,1 / 2,1,1,1 / 1,2,2 / 2,1,2
      2,2,1 / 3,1,1 / 1,3,1 / 1,1,3 / 2,3 / 3,2 = 13
      
n[4] = n[3] + n[2] + n[1]
n[5] = n[4] + n[3] + n[2]
n[i] = n[i-1] + n[i-2] + n[i-3]
'''