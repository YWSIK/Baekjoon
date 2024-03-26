def solution(n, words):
    #같은 단어를 말하면 탈락, 이어지지 않아도 탈락
    #몇번째 인원이 탈락하는 지, 몇번째 턴에 탈락하는 지

    used = set() #사용한 단어 저장
    prev = words[0]
    used.add(prev)
    
    for i in range(1, len(words)):
        curr = words[i]
        
        if curr in used or curr[0] != prev[-1]:
            return [(i % n)+1, (i // n)+1]

        else:
            used.add(curr)
            prev = curr
    
    return [0, 0]