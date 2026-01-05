import sys

input = sys.stdin.readline
write = sys.stdout.write

M = int(input())
S = 0

for _ in range(M):
    cmd = input().rstrip()

    c = cmd[0]

    if c == 'a':
        if cmd[1] == 'd':      # add
            x = int(cmd[4:])
            S |= (1 << (x - 1))
        else:                  # all
            S = (1 << 20) - 1

    elif c == 'r':             # remove
        x = int(cmd[7:])
        S &= ~(1 << (x - 1))

    elif c == 'c':             # check
        x = int(cmd[6:])
        write('1\n' if (S & (1 << (x - 1))) else '0\n')

    elif c == 't':             # toggle
        x = int(cmd[7:])
        S ^= (1 << (x - 1))

    else:                      # empty
        S = 0
