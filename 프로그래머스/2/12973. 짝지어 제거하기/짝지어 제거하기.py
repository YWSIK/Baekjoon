def solution(s):
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i]) #첫번째부터 스택에 삽입
            
        elif s[i] == stack[-1]: #top원소와 현 문자열 비교
            stack.pop() #같으면 빼냄
            
        else:
            stack.append(s[i])
            
    if len(stack) == 0:
        return 1
    
    else:
        return 0