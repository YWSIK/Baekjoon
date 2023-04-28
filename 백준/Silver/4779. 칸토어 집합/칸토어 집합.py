#4779
#3^n

def Cantorset(n):
    if n == 0:
        return '-'
    else:
        prev = Cantorset(n-1)
        blank = ' ' * (3**(n-1))
        return prev + blank + prev
    
while True:
    try:
        n = int(input())
        print(Cantorset(n))
    except:
        break