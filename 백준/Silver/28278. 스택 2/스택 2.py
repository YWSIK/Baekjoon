#28278
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
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return 1 if not self.stack else 0
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1
    
def process_commands(commands):
    stack = Stack()
    result = []
    
    for command in commands:
        if command[0] == 1:  # Push
            stack.push(command[1])
        elif command[0] == 2:  # Pop
            result.append(stack.pop())
        elif command[0] == 3:  # Size
            result.append(stack.size())
        elif command[0] == 4:  # Empty
            result.append(stack.empty())
        elif command[0] == 5:  # Top
            result.append(stack.top())
    return result


n = int(sys.stdin.readline())
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = process_commands(commands)
for output in result:
    print(output)