#5622
dial = {
    'ABC': 2, 'DEF': 3, 'GHI': 4,
    'JKL': 5, 'MNO': 6, 'PQRS': 7,
    'TUV': 8, 'WXYZ': 9
}

result = 0

num = input()

for char in num:
    for key in dial:
        if char in key:
            result += dial[key] + 1
            break
        
print(result)