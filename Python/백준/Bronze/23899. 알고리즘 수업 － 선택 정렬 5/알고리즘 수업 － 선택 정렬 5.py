import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
if a == b:
    print(1)
    exit()
for i in range(n, 1, -1):
    idx, large = max(enumerate(a[:i]), key=lambda x: x[1])
    if idx != i-1:
        a[idx], a[i-1] = a[i-1], a[idx]
    if a == b:
        print(1)
        exit()
print(0)