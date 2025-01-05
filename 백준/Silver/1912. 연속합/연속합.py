#1912
# 양수가 나오면 더하다가 
# 음수가 나올 때 그 음수가 지난 양수들의 합을 음수로 만들면 다음으로
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split(" ")))

cur_sum = nums[0]
max_sum = nums[0]

for i in range(1, len(nums)):
    cur_sum = max(nums[i], cur_sum + nums[i])
    max_sum = max(max_sum, cur_sum)
    
print(max_sum)
