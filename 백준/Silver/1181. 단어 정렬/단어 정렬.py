#1181
import sys

n = int(sys.stdin.readline())
words = []

for i in range(n):
    word = input()
    words.append(word)
    
words = list(set(words))
words.sort()

words.sort(key=lambda x : len(x))

for word in words:
    print(word)