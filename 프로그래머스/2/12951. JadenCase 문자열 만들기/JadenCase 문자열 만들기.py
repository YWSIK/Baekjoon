def solution(s):
    arr = s.split(' ')
    arr2 = []
    
    for i in arr:
        # if i[0].isdigit():
        #     arr2.append(i)
        # else:
        arr2.append(i.capitalize())
    
    return ' '.join(arr2)
    
    