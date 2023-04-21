#2164
import sys
from collections import deque

num = int(sys.stdin.readline())
cards = deque(range(1, num + 1))

while (len(cards) > 1):
   
    cards.popleft()
    remove = cards.popleft()
    cards.append(remove)

print(cards[0])