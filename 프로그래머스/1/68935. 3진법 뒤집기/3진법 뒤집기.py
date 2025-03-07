def solution(n):
    num_3 = []
    result = 0
    
    while n > 0:
        num_3.append(n%3)
        n //= 3
    
    for i in range(len(num_3)): 
        result += num_3[i] * (3 ** (len(num_3) - i - 1))
    return result