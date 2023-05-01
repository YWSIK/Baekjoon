import sys

num = int(sys.stdin.readline())
arr = []

for i in range(1, num):
    digits_sum = sum([int(digit) for digit in str(i)])
    if i + digits_sum == num:
        arr.append(i)

if arr:
    print(min(arr))

else:
    print(0)