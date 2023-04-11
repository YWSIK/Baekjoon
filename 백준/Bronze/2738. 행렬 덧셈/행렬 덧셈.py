#2738
try:
    N, M = map(int, input().split())
    matrix1 = []
    matrix2 = []
    matrix = [[0] * M for _ in range(N)]

    for i in range(N):
        matrix1.append(list(map(int, input().split(" "))))
        
    for i in range(N):
        matrix2.append(list(map(int, input().split(" "))))

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end=" ")
        print()

except EOFError:
    pass
