#12789

import sys

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1

def check_order(n, queue):
    stack = Stack()
    exp = 1 # 원하는 번호
    
    for num in queue:
        # 스택 비어있지 않고, 맨 위가 기대값이면 pop 하고 exp 1 증가
        while stack.stack and stack.stack[-1] == exp:
            stack.pop()
            exp += 1
        
        # 현재 번호가 기대값이면 다음 번호로
        if num == exp:
            exp += 1
        # 아니면 스택에 현 번호 추가
        else:
            stack.push(num)
    
    #가장 위 번호를 빼서 기대값과 비교 후 다르면 순서대로가 아님       
    while stack.stack:
        if stack.pop() != exp:
            return "Sad"
        exp += 1
        
    return "Nice"

n = int(sys.stdin.readline())
queue = list(map(int, sys.stdin.readline().split()))

print(check_order(n, queue))