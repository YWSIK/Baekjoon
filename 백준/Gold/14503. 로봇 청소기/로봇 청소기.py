import sys
input = sys.stdin.readline

#방의 크기
n, m = map(int, input().split())
#시작 좌표(r, c), d가 0(북), 1(동), 2(남), 3(서)
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

#방향: 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cleaned = [[False] * m for _ in range(n)]
cnt = 0

while True:
    # 1. 현재 칸이 아직 청소되지 않았다면 청소
    if not cleaned[r][c]:
        cleaned[r][c] = True
        cnt += 1
    
    # 2. 주변 4칸 중 청소 안 된 칸이 있는지 확인
    found = False
    for _ in range(4):
        d = (d-1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        
        # 청소되지 않았다면 전진
        if room[nr][nc] == 0 and not cleaned[nr][nc]:
            r, c = nr, nc
            found = True
            break
        
        # 3. 4방향 모두 청소할 곳이 없는 경우
    if not found:
            # 뒤로 후진
        back_d = (d+2) % 4
        br = r + dr[back_d]
        bc = c + dc[back_d]
            
            # 뒤가 벽이면 종료
        if room[br][bc] == 1:
                break
            
            # 뒤가 벽이 아니면 후진
        r, c = br, bc
            
print(cnt)