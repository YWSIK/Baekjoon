def solution(s):
    result = 0
    
    for i in s:
        if i == "(":
            result += 1
        
        elif i == ")":
            if result == 0:
                return False
            result -= 1
            
    if result == 0:
        return True
    
    else:
        return False