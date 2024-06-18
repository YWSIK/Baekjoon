from collections import deque
import math

def solution(progresses, speeds):
    # 각 기능이 완료되는 날짜 계산
    days = deque([math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)])
    
    answer = []
    
    while days:
        current_release_day = days.popleft()
        count = 1
        
    # 큐에서 pop하면서 같은 날 배포 가능한 기능의 수를 센다
        while days and days[0] <= current_release_day:
            days.popleft()
            count += 1
        
        answer.append(count)
    
    return answer