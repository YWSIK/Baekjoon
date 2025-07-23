#1259
import sys

for line in sys.stdin:
    n = line.strip()
    
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')