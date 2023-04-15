#25305
# N=응시생, k=상 받는 인원
N, k = map(int, input().split())

# points = []
# for i in range(N):
#     point = int(input().split(" ")) #하나씩 입력 받는거
#     points.append(point)

points = list(map(int, input().split())) #한번에 입력 받기
points.sort(reverse=True) #내림차순
print(points[k-1])