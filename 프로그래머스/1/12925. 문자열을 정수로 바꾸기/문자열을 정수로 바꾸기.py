def solution(s):
    if not (1 <= len(s) <= 5):
        return False
    
    elif s[0] == "0":
        return False
    
    else:
        answer = int(s)
        return answer