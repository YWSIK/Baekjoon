def solution(arr1, arr2):
    result = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(arr1)):           # arr1의 행을 반복
        for j in range(len(arr2[0])):    # arr2의 열을 반복
            for k in range(len(arr2)):   # arr1의 열과 arr2의 행을 반복
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result