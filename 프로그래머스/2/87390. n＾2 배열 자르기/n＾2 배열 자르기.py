def solution(n, left, right):
    arr = []
    
    for idx in range(left, right+1):
        row = idx // n
        col = idx % n
        arr.append(max(row+1, col+1))
        
    return arr