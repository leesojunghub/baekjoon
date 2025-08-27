import sys
r, b = map(int, sys.stdin.readline().strip().split())
total = r + b
for i in range(int(total**0.5), 0, -1):
    if total % i == 0:
        if b % (i - 2) == 0 and b % (total // i - 2) == 0:
            print(total // i, i)
            break