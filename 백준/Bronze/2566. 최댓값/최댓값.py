#2566
matrix = [[0] * 9 for _ in range(9)]

#1열부터 차례로 입력받음
for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        matrix[i][j] = row[j]

max = 0
result_i = 0
result_j = 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max:
            max = matrix[i][j]
            result_i = i
            result_j = j

print(max)
print(result_i + 1, result_j + 1)