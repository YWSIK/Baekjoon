#1969
import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    n, m = map(int, input().split())
    dna = [input() for _ in range(n)]
    
    consensus = ''
    hamming_distance = 0
    
    for i in range(m):
        cnt = {'A':0, 'C':0, 'G':0, 'T':0}
        
        for j in range(n):
            cnt[dna[j][i]] += 1
            
        max_char = min(cnt, key=lambda x: (-cnt[x], x))
        consensus += max_char
        
        for j in range(n):
            if dna[j][i] != max_char:
                hamming_distance += 1
                
    print(consensus)
    print(hamming_distance)
    
solve()