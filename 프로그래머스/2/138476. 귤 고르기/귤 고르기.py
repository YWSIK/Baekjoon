def solution(k, tangerine):
    from collections import Counter
    
    size_cnt = Counter(tangerine)
    
    sorted_sizes = sorted(size_cnt.values(), reverse = True)
    
    total = 0
    cnt = 0
    
    for size in sorted_sizes:
        total += size
        cnt += 1
        
        if total >= k:
            return cnt