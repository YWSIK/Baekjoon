#17413
import sys

def input():
    return sys.stdin.readline().rstrip()


def reverse_words(S):
    result = []
    word = []
    in_tag = False
    
    for char in S:
        if char == '<':
            if word:
                result.append(''.join(word[::-1]))
                word = []
            in_tag = True
            result.append(char)
        elif char == '>':
            in_tag = False
            result.append(char)
        elif in_tag:
            result.append(char)
        else:
            if char == ' ':
                if word:
                    result.append(''.join(word[::-1]))
                    word = []
                result.append(char)
            else:
                word.append(char)
                
    if word:
        result.append(''.join(word[::-1]))
        
    return ''.join(result)

S = input()
print(reverse_words(S))