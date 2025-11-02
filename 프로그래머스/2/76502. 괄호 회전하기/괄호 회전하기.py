def solution(s):
    def is_valid(arr):
        stack = []
        pairs = {')':'(', ']': '[', '}': '{'}
        
        for a in arr:
            if a in '([{':
                stack.append(a)
            else:
                if not stack or stack[-1] != pairs[a]:
                    return False
                stack.pop()
        return not stack
    cnt = 0
    for i in range(len(s)):
        r = s[i:] + s[:i]
        if is_valid(r):
            cnt += 1
    return cnt