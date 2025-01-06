#1018
n, m = map(int, input().split())

board = [input() for _ in range(n)]

chess_board1 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

chess_board2 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

#다시 칠해야하는 칸 계산산
def count_repaints(x, y, pattern):
    cnt = 0
    
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != pattern[i][j]:
                cnt += 1
                
    return cnt

min_repaints = float("inf")

for i in range(n-7):
    for j in range(m-7):
        repaints1 = count_repaints(i, j, chess_board1)
        repaints2 = count_repaints(i, j, chess_board2)
        
        min_repaints = min(min_repaints, repaints1, repaints2)
        
print(min_repaints)