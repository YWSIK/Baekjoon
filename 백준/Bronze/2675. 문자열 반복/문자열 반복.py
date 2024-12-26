#2675
n = int(input())

for _ in range(n):
    num, s = input().split()
    num = int(num)
    
    P = ''.join(char * num for char in s)

    print(P)