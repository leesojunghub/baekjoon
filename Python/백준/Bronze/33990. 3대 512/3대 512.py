import sys
n = int(sys.stdin.readline().strip())
a = 601
for _ in range(n):
    l = list(map(int, sys.stdin.readline().strip().split()))
    if sum(l)>=512:
        if sum(l) < a:
            a = sum(l)
if a == 601:
    print(-1)
else:
    print(a)