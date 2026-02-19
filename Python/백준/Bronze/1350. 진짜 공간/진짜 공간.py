import sys
n = int(sys.stdin.readline())
file = list(map(int, sys.stdin.readline().split()))
cluster = int(sys.stdin.readline())
total = 0
for i in file:
    if i % cluster == 0:
        total += i
    else:
        total += (i // cluster + 1) * cluster
print(total)