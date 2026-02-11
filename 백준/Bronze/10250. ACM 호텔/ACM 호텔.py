#10250
# n // h 호수, n % h 층수
T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split(" "))
    floor = n % h
    room = (n-1) // h + 1
    if floor == 0:
        floor = h
    
    print(f"{floor}{room:02d}")