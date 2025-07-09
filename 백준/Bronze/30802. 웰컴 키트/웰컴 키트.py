#30802
import math

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

shirt_bundles = sum(math.ceil(size / t) for size in sizes)
print(shirt_bundles)

pen_bundle = n // p
pen_single = n % p
print(pen_bundle, pen_single)