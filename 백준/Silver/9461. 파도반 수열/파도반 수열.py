#9461
# p1, 1 - p2, 1 - p3, 1 - p4, 2 - p5, 2 - 
# p6, 3 - p7, 4 - p8, 5 - p9, 7 - p10, 9
# p[i] = p[i-1] + p[i-5]

T = int(input())

p = [0] * 101
p[1], p[2], p[3], p[4], p[5] = 1, 1, 1, 2, 2

for i in range(6, 101):
    p[i] = p[i] = p[i-1] + p[i-5]

for _ in range(T):
    n = int(input())
    print(p[n])