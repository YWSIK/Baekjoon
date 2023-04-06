subject = int(input())  # 과목 수
score = list(map(int, input().split()))
max_score = max(score)

new_score = []
for s in score :
    new_score.append(s / max_score *100)  # 새로운 점수 생성
avg = sum(new_score) / subject
print(avg)
