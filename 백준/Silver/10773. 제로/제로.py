#10773
import sys

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, num):
        self.stack.append(num)
        
    def pop(self):
        return self.stack.pop()
    
    def summary(self):
        return sum(self.stack)

stack = Stack()
k = int(sys.stdin.readline())

for _ in range(k):
    number = int(sys.stdin.readline())
    if number == 0:
        stack.pop()
    else:
        stack.push(number)
        
print(stack.summary())