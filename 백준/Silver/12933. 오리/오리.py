#12933
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    sounds = input()
    duck = "quack"

    if len(sounds) % len(duck) != 0:
        print(-1)
        return
    
    ducks = [0] * len(sounds)
    
    duck_cnt = 0
    for sound in sounds:
        found = False
        
        for i in range(duck_cnt):
            if duck[ducks[i]] == sound:
                ducks[i] += 1
                if ducks[i] == len(duck):
                    ducks[i] = 0
                found = True
                break
            
        if not found:
            if sound == 'q':
                ducks[duck_cnt] = 1
                duck_cnt += 1
            else:
                print(-1)
                return
            
    if any(ducks[i] != 0 for i in range(duck_cnt)):
        print(-1)
    else:
        print(duck_cnt)
    
solve()