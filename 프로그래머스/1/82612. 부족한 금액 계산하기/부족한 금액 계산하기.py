def solution(price, money, count):
    result = 0
    for i in range(1, count+1):
        result += price * i
    
    if (result - money) > 0:
        return abs(result - money)
    else:
        return 0