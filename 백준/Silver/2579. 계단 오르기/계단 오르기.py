#2579
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
score = [0] + [int(input()) for i in range(n)]
dp = [0] * (n+1)

if n == 1:
    print(score[1])

else:    
    dp[1] = score[1]
    
    if n >= 2:
        dp[2] = score[1] + score[2]
    if n >= 3:
        dp[3] = max(score[1] + score[3], score[2] + score[3])
    
    for i in range(4, n+1):
        #두 칸 전에서 건너 뛰고옴 vs 세 칸 전에서 직전 계단 찍고 현재로
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
        
    print(dp[n])
'''
많이 밟는게 좋음.단 연속 세 개 불가
dp[3] = score[1] + score[3] vs score[2] + score[3]
dp[4] = score[1] + score[2] + score[4] vs score[2] + score[3] vs score[1] + score[3] + score[4]

하나 밟고 넘어갈 지, 두개 밟고 넘어갈 지.
dp[i-2] + score[i] vs dp[i-3]
'''