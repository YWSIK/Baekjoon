#participant = 참가자, completion = 완주, answer = 완주X

def solution(participant, completion):

    #동명이인 없을 때
    complete = list(set(participant)-set(completion))
    if len(complete) != 0:
        return complete[0]
    
    #동명이인 있을 때
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]
            
    answer = ''
    return answer