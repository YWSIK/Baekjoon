#11718
import sys

s = sys.stdin.readlines()
for i in s:
    print(i.rstrip())

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break