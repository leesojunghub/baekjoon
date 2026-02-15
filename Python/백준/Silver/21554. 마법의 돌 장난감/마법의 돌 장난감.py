import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
lr = []
i = 0
cor = list(range(1, n + 1))
while i < n and cnt <= 100:
    if a[i] != i+1:
        j = a.index(i + 1)
        a[i:j+1] = reversed(a[i:j+1])
        cnt += 1
        lr.append((i+1,j+1))
    i += 1
if a != cor:
    print(-1)
else:
    print(cnt)
    for i in lr:
        print(i[0], i[1])