from collections import Counter

def solution(nums):
    choice = len(nums) // 2
    diffnum = len(set(nums))
    
    if (choice >= diffnum):
        return diffnum
    else:
        return choice

# [1, 2, 3, 4] -> 2
# [1, 1, 1, 3, 3, 3] -> 2
# choice 보다 서로 다른 숫자의 개수가 많음 -> choice
# choice 보다 서로 다른 숫자의 개수가 적음 -> 숫자 종류의 수