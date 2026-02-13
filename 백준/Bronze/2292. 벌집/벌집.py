#2292
# 1 6 12 18...

n = int(input())

layer = 1
end = 1

while n > end:
    end += 6 * layer
    layer += 1
    
print(layer)