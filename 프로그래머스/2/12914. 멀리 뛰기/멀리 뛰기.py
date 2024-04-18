def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        
    return dp[n]
        
# n = 5
# 1칸 1칸 1칸 1칸 1칸 -> 1
# 1칸 1칸 1칸 2칸 / 1칸 1칸 2칸 1칸 / 1칸 2칸 1칸 1칸 / 2칸 1칸 1칸 1칸 -> 4
# 1칸 2칸 2칸 / 2칸 1칸 2칸 / 2칸 2칸 1칸 -> 3