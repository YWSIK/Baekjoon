def solution(triangle):
    triangle = triangle[::-1]
    
    # 맨 아래에서 한 칸 위
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j+1])
            
    return triangle[-1][0]
            