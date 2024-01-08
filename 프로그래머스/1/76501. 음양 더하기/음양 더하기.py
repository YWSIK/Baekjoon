def solution(absolutes, signs):
    
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = (-1) * absolutes[i] 
            
    return sum(absolutes)