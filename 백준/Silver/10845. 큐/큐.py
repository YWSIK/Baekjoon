#10845
import sys
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, num):
        self.queue.append(num) #정수 삽입

    def pop(self):
        if self.empty():
            return -1
        return self.queue.popleft() #들어있는거 없으면 0

    def size(self):
        return len(self.queue)

    def empty(self):
        return 1 if not self.queue else 0 #스택이 비면 0
    
    def front(self):
        if self.empty():
            return -1
        return self.queue[0] # 들어있는거 없으면 0
    
    def back(self):
        if self.empty():
            return -1
        return self.queue[-1] # 맨 뒤 제거

n = int(sys.stdin.readline())
queue = Queue()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.push(int(command[1])) #숫자 삽입
    elif command[0] == 'pop':
        print(queue.pop())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'back':
        print(queue.back())
    elif command[0] == 'empty':
        print(queue.empty())