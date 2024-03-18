def solution(n):
    
    result = 1 # n 자기 자신
    
    for i in range(1, n//2 + 1):
        sum_n = 0
        
        while sum_n < n:
            sum_n += i
            
            if sum_n == n:
                result += 1
                break
                
            i += 1
            
    return result