def solution(s):
    remove_zero = 0
    remove_times = 0
    
    while True:
        if s == "1":
            break;
            
        remove_times += 1
        remove_zero += s.count("0")
        
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        
    return [remove_times, remove_zero]
        
        