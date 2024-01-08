def solution(s):
    num_list = list(int(i) for i in s.split(" "))

    return f"{min(num_list)} {max(num_list)}"