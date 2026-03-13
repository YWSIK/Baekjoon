import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

students = []

for i in range(n):
    students.insert(i - arr[i], i + 1)

print(*students)