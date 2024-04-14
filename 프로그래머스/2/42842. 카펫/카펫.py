def solution(brown, yellow):
    a = 1
    
    while True:
        b = (brown - 2*a + 4)/2
        
        if ((a-2) * (b-2)) == yellow:
            break
        
        a += 1
        
    return [int(b), a]