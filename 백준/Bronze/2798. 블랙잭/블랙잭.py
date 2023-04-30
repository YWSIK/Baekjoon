#2798
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
maxsum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_arr = arr[i] + arr[j] + arr[k]
            if sum_arr <= M:
                maxsum = max(maxsum, sum_arr) #둘 중 큰 값을 maxsum에 저장

print(maxsum)