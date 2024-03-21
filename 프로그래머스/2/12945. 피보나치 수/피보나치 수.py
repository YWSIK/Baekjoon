def solution(n):
    fiblist = [1, 1]
    
    if n == 1 or n == 2:
        return 1
    
    for i in range(2, n):
        fiblist.append(fiblist[i-1] + fiblist[i-2])
    
    return fiblist[-1] % 1234567