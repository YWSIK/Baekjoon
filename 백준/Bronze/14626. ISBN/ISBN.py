#14626
import sys
input = sys.stdin.readline

arr = input().strip()
base = 0
star_idx = -1

for i in range(13):
    if arr[i] == '*':
        star_idx = i
        continue
        
    w = 1 if i % 2 == 0 else 3
    base += int(arr[i]) * w
    
star_w = 1 if star_idx % 2 == 0 else 3
for j in range(10):
    if (base + j * star_w) % 10 == 0:
        print(j)
        break