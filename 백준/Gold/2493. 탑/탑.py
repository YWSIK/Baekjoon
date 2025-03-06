#2493
import sys

def input():    return sys.stdin.readline().rstrip()

def build_top():
    n = int(input())
    receive = [0] * n
    stack = [] # (idx, height) 로 저장
    h = list(map(int, input().split(" ")))
    
    for i in range(n):
        while stack and stack[-1][1] < h[i]:
            stack.pop()

        if stack:
            receive[i] = stack[-1][0] + 1

        stack.append((i, h[i]))
        
    print(" ".join(map(str, receive)))
    
build_top()