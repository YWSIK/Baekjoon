#1152
s = input()
cnt = s.count(" ")

if s[0] == " ":
    cnt -= 1
    
if s[-1] == " ":
    cnt -= 1

print(cnt+1)