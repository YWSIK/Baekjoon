#28702
import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(3)]

num = None
idx = None

for i, s in enumerate(arr):
    if s.isdigit():
        num = int(s)
        idx = i
        break
    
last = num + (2-idx)
x = last + 1

if x % 15 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)