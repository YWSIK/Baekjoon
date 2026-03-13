"""
https://www.acmicpc.net/problem/1244?utm_source=chatgpt.com
"""
"""
1 : 켜짐 / 0 : 꺼짐
1 이상, 스위치 개수 이하인 자연수 하나씩 가짐
남자 : 스위치 번호가 자기 숫자 배수면 상태를 바꿈
여자 : 스위치 번호 좌우가 대칭 -> 변경 / 아닐 시 스위치 번호만 변경

남학생 1 여학생 2
"""

import sys
input = sys.stdin.readline

n = int(input()) # 스위치 개수
switch_state = list(map(int, input().split())) # 스위치 초기 상태
m = int(input()) # 학생 수
students = []

for _ in range(m):
    sex, num = map(int, input().split())
    
    if sex == 1: # 남자면
        for i in range(num-1, n, num):
            switch_state[i] = 1 - switch_state[i]

    else: # 여자면
        left = num-1
        right = num-1
        
        while left - 1 >= 0 and right + 1 < n and switch_state[left-1] == switch_state[right+1]:
            left -= 1
            right += 1
            
        for i in range(left, right+1):
            switch_state[i] = 1 - switch_state[i]

for i in range(n):
    print(switch_state[i], end= ' ')
    if (i+1) % 20 == 0:
        print()