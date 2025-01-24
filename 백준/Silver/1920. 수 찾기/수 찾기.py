#1920
n = int(input())
nums = set(map(int, input().split()))

m = int(input())
is_in_nums = list(map(int, input().split()))

for i in is_in_nums:
    if i in nums:
        print(1)
    else:
        print(0)