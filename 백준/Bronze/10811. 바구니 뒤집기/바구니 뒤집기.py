N, M = map(int, input().split())
basket = [i for i in range(1, N+1)] # 1 부터 N 까지

for _ in range(M):
    i, j = map(int, input().split())
    r = j - i + 1 # i 부터 j 까지
    for _ in range(r // 2): # 두번씩 바꾸면 됨
        basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
        # temp = basket[i-1]
        # basket[i-1] = basket[j-1]
        # basket[j-1] = temp
        i += 1
        j -= 1

for _ in basket:
    print(_, end=' ')