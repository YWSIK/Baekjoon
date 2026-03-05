#2869
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

if V <= A:
    print(1)
else:
    daily = A - B
    remain = V - A
    days_before_last = (remain + daily - 1) // daily
    print(days_before_last + 1)