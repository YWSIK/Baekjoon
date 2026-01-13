from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    
    def compare(a, b):
        # a가 앞에 와야 하면 음수
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    numbers.sort(key=cmp_to_key(compare))
    
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer
