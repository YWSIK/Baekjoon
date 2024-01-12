def solution(num, result = 0):
    
    if num == 1:
        return result
    
    elif result >= 500:
        return -1
    
    else:
        if num % 2 == 0:
            return solution(num // 2, result+1)
        else:
            return solution(num * 3 + 1, result+1)