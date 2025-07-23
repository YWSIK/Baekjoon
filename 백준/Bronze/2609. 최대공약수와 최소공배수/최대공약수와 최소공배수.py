#2609
import math

n, m = map(int, input().split(' '))

gcd = math.gcd(n, m)
lcm = n*m // gcd

print(gcd)
print(lcm)

# n, m = map(int, input().split(' '))

# def get_gcd(x, y):
#     while y:
#         x, y = y, x % y
#         return x

# gcd = get_gcd(n, m)
# lcm = n*m // gcd

# print(gcd)
# print(lcm)