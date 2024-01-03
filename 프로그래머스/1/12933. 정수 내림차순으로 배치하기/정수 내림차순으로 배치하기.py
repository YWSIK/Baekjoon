def solution(n):
    n = str(n)
    list = []
    
    for i in range(0, len(n)):
        list.append(n[i])
    
    list.sort(reverse = True)
    
    return int(''.join(list))
        