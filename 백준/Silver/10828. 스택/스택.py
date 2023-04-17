#10828
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.empty():
            return -1
        return self.stack.pop()

    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def empty(self):
        return int(self.size() == 0)


stack = Stack()
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'top':
        print(stack.top())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
