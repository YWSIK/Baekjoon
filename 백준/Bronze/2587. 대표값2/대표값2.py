#2587
nums = []

for i in range(5):
    num = int(input())
    nums.append(num)
    
nums.sort()
middle = nums[2]

print(int(sum(nums) / 5))
print(middle)