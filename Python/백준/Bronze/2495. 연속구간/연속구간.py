import sys
for _ in range(3):
    s = list(sys.stdin.readline().strip())
    cnt = 1
    start = s[0]
    best = 1
    for i in range(1, 8):
        if s[i] == start:
            cnt += 1
        else:
            if cnt > best:
                best = cnt
            cnt = 1
            start = s[i]
    if cnt > best:
        best = cnt
    print(best)