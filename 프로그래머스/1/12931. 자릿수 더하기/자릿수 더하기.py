def solution(n):
    n = str(n)
    sum = 0
    
    for i in range(0, len(n)):
        sum += int(n[i])    

    return sum