def solution(n):

    n_cnt = bin(n)[2:].count('1')
    
    for i in range(n+1, 2*n+1):
        next_cnt = bin(i)[2:].count('1')
        
        if n_cnt == next_cnt:
            return i