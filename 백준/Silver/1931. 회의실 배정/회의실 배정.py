#1931
n = int(input())
time = []
cnt = 0
last_time = 0

for _ in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

#종료시간 기준으로 정렬
time.sort(key=lambda x: (x[1], x[0]))

for interval in time:
    start, end = interval
    
    #회의 시작이 마지막 회의 종료 시간 이후여야 함
    if start >= last_time:
        cnt += 1
        last_time = end

print(cnt)