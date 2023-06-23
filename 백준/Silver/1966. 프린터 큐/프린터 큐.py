#1966
from collections import deque

test = int(input())

for i in range(test):
    n, m = map(int, input().split()) #n=개수 m=원하는 문서 번호(0부터 시작)
    queue = deque(list(map(int, input().split())))
    cnt = 0
    
    while queue:
        imp = max(queue) 
        front = queue.popleft() #중요도 가장 큰 애 pop
        m -= 1 #내 위치 당김
        
        if imp == front: #처음이 가장 크면 cnt + 1
            cnt += 1
            if m < 0:
               print(cnt)
               break
           
        else:
            queue.append(front) #뒤로 밈
            if m < 0:
                m = len(queue)-1