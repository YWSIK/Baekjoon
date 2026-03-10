"""
T = 걸리는 시간
P = 받는 금액
"""

import sys
input = sys.stdin.readline

n = int(input())
schedule_list = []
index = 0
prob_schedule = [0] * (n+1)

for _ in range(n):
    t, p = map(int, input().split())
    schedule_list.append((t,p))
    
for i in range(n-1, -1, -1):
    t, p = schedule_list[i]
    
    if i + t <= n:
        prob_schedule[i] = max(prob_schedule[i+1], p + prob_schedule[i+t])
    else:
        prob_schedule[i] = prob_schedule[i+1]
        
print(prob_schedule[0])