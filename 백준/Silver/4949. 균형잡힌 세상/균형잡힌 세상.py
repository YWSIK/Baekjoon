#4949
import sys

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, words):
        self.stack.append(words)
        
    def pop(self):
        if not self.stack:
            return False
        else:
            return self.stack.pop()
    
    def empty(self):
        return not bool(self.stack)
    
def check_vps(string):
    stack = Stack()
    for s in string:
        if s == '(' or s == '[':
            stack.push(s)
        elif s == ')' :
            if stack.pop() != '(':
                return "no"
        elif s == ']':
            if stack.pop() != '[':
                return "no"
    if stack.empty():
        return "yes"
    else:
        return "no"

while True:
    string = sys.stdin.readline().rstrip()
    if string == ".":
        break
    print(check_vps(string))
