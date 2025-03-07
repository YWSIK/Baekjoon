def solution(s):
    words = s.split(" ")
    result = []
    
    for word in words:
        new_word = ''
        for j in range(len(word)):
            if j % 2 == 0:
                new_word += word[j].upper()
            else:
                new_word += word[j].lower()
        result.append(new_word)
                
    return ' '.join(result)