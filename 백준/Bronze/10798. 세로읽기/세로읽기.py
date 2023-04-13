
arr = [0 for _ in range(5)] #문자열 5개
result = ['' for _ in range(15)] #최대 15개

for i in range(5):
    arr[i] = list(input()) #한글자씩 분리해서 저장

for i in range(15):
    for j in range(5):
        if i < len(arr[j]): #j번째 열의 길이보다 i가 작을때만 더함
            result[i] += arr[j][i] #짧으면 빈문자열 추가해 길이 유지

print(''.join(result)) #문자열 결합