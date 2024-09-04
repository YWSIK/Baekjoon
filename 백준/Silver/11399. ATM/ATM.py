#11399
n = int(input())

people = []
cnt = 0
summ = 0

people = list(map(int, input().split()))
people.sort()

for i in people:
    cnt += i
    summ += cnt

print(summ)