#1436
# 6이 최소 3개가 연속해야함.

n = int(input())
end_num = 666
cnt = 0

while True:
    if '666' in str(end_num):
        cnt += 1
        
        if cnt == n:
            print(end_num)
            break
        
    end_num += 1