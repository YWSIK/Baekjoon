import sys

num = int(sys.stdin.readline())
stack = []
result = []
count = 1

for i in range(num):
    n = int(sys.stdin.readline())

    while count <= n:
        stack.append(count)
        count += 1
        result.append('+')
    
    if stack[-1] == n:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0) #프로그램을 정상적으로 종료

print('\n'.join(result))