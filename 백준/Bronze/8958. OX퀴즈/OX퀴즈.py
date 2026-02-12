import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    result = sys.stdin.readline().strip()
    
    score = 0
    streak = 0
    
    for ch in result:
        if ch == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    
    print(score)