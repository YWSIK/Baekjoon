#2920
arr = list(map(int, input().split(' ')))

diffs = [arr[i+1] - arr[i] for i in range(7)]

if all(d == 1 for d in diffs):
    print("ascending")
elif all(d == -1 for d in diffs):
    print("descending")
else:
    print("mixed")