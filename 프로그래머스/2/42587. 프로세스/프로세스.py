from collections import deque, Counter

def solution(priorities, location):
    queue = deque(
        (p, i == location) for i, p in enumerate(priorities)
    )
    
    count = Counter(priorities)
    current_max = max(count)
    order = 0
    
    while queue:
        priority, is_target = queue.popleft()
        
        if (priority == current_max):
            order += 1
            count[priority] -= 1
            
            if count[priority] == 0:
                del count[priority]
                if count:
                    current_max = max(count)
            
            if is_target:
                return order
        else:
            queue.append((priority, is_target))