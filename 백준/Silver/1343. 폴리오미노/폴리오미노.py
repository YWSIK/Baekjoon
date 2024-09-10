#1343
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    board = input()
    result = ""

    i = 0
    while i < len(board):
        if board[i] == 'X':
            cnt = 0
            #연속된 X의 개수
            while i < len(board) and board[i] == 'X':
                cnt += 1
                i += 1

            if cnt % 2 == 1: #X 개수가 홀수면 -1
                print(-1)
                return
                
            result += 'AAAA' * (cnt // 4)
            cnt %= 4
            result += 'BB' * (cnt // 2)
        else:
            result += '.'
            i += 1
            
    print(result)
    
solve()