n = int(input())

def hanoi(n, s, e): #원 개수, 출발, 목적지
    if n == 1:
        print(s, e)
        return
    
    hanoi(n-1, s, 6-s-e)
    print(s, e)
    hanoi(n-1, 6-s-e, e)
    
print(2**n-1)
hanoi(n, 1, 3)