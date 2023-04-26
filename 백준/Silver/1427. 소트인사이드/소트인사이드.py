#1427
n = input()

nums = list(map(int, n))
nums = sorted(nums, reverse=True)

result = ''.join(map(str, nums))
print(result)