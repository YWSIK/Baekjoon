#22864
import sys

def input():
    return sys.stdin.readline().rstrip()

#하루는 24시간
#a: 한 시간 일 하면 쌓이는 피로도
#b: 한 시간 동안 처리 가능한 일의 양
#c: 한 시간 쉬면 줄어드는 피로도
#m: 피로도의 최대치
a, b, c, m = map(int, input().split())
work = 0
time = 0
tired = 0

if a > m:
    print('0')

else:
    while (time < 24):
        if tired + a <= m: #일을 하는 경우
            work += b
            tired += a
            time += 1
        else:
            if tired + a > m: #휴식하는 경우
                tired -= c
                if tired < 0: #피로도 0 미만 X
                    tired = 0
                time += 1
    
    print(work)