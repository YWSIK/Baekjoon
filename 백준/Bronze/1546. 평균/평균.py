#1546
# 점수 중 최댓값 M, 모든점수를 점수 / M * 100 으로

subject = int(input())  # 과목수
score = list(map(int, input().split()))
max_score = max(score)

new_score = []
for s in score :
    new_score.append(s / max_score *100)  # 새로운 점수
avg = sum(new_score) / subject
print(avg)
