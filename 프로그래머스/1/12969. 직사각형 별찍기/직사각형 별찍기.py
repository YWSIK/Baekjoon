a, b = map(int, input().strip().split(' '))

cnt = 0

for i in range(b):
    for j in range(a):
        print('*', end='')
        cnt += 1
        if cnt == a:
            cnt = 0
            print(end='\n')