def solution(arr):
    lcm_value = arr[0]
    
    for num in arr[1:]:
        lcm_value = lcm(lcm_value, num)
    
    return lcm_value

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)