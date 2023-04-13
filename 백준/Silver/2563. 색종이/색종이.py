#2563
arr = [[0] * 101 for _ in range(101)]

for _ in range(int(input())): #색종이 수 입력
    p1, p2 = map(int, input().split(" "))
    for i in range(10):
        for j in range(10):
            arr[p1+i][p2+j] = 1 #위아래 열 칸씩 1로 만들기

result = 0
for i in arr: #arr을 돌면서 있는 값들 더 함
    result += sum(i)
print(result)