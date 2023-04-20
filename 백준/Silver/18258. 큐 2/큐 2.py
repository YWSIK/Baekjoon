#18258
import sys
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, num):
        self.queue.append(num)
        
    def pop(self):
        if self.empty():
            return -1
        return self.queue.popleft()
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return int(self.size() == 0)
    
    def front(self):
        if self.empty():
            return -1
        return self.queue[0]
    
    def back(self):
        if self.empty():
            return -1
        return self.queue[-1]

queue = Queue()
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.push(int(command[1])) #숫자 삽입
    elif command[0] == 'pop':
        sys.stdout.write(str(queue.pop())+'\n')
    elif command[0] == 'top':
        sys.stdout.write(str(queue.top())+'\n')
    elif command[0] == 'size':
        sys.stdout.write(str(queue.size())+'\n')
    elif command[0] == 'empty':
        sys.stdout.write(str(queue.empty())+'\n')
    elif command[0] == 'front':
        sys.stdout.write(str(queue.front())+'\n')
    elif command[0] == 'back':
        sys.stdout.write(str(queue.back())+'\n')
