import sys
n, x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
window = sum(l[:x])
best = window
count = 1
for i in range(x, n):
    window = window + l[i] - l[i-x]
    if window > best:
        best = window
        count = 1
    elif window == best:
        count += 1
if best == 0:
    print('SAD')
else:
    print(best)
    print(count)