def solution(n):

    bin_n = bin(n)[2:]
    cnt = bin_n.count('1')
    
    for i in range(n+1, 2*n+1):
        bin_i = bin(i)[2:]
        next_cnt = bin_i.count('1')
        
        if cnt == next_cnt:
            return i