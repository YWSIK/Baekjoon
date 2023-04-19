#9012
import sys

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, bracket):
        self.stack.append(bracket)
    
    def pop(self):
        if not self.stack:
            return False #스택이 비어있는 경우
        else:
            return self.stack.pop()
        
    def is_empty(self):
        return not bool(self.stack)
    #비어 있으면 True, 아니면 False
    
def check_vps(string):
    stack = Stack()
    for s in string:
        if s == '(':
            stack.push(s)
        elif s == ')':
            if stack.pop() == False:
                return "NO" #비어 있으면 NO
    if stack.is_empty():
        return "YES" #True면 YES
    else:
        return "NO"
            
n = int(sys.stdin.readline())
for i in range(n):
    string = sys.stdin.readline().rstrip()
    print(check_vps(string))