from collections import Counter

def solution(clothes):
    clothes_count = Counter([kind for name, kind in clothes])
    
    cb = 1
    for cnt in clothes_count.values():
        cb *= (cnt + 1)    
    
    return cb - 1