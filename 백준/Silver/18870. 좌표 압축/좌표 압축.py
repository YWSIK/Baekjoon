#18870
n = int(input())
arr = list(map(int, input().split()))

#좌표 오름차순으로 정렬 + 중복 제거
sorted_arr = sorted(set(arr))

#값이 몇 번째인지 매핑
dic = {value: idx for idx, value in enumerate(sorted_arr)}

#압축된 값으로 변환
after_arr = [dic[x] for x in arr]

print(' '.join(map(str, after_arr)))