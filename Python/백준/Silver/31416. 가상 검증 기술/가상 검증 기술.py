import sys
t = int(sys.stdin.readline())
for _ in range(t):
    ta, tb, va, vb = map(int, sys.stdin.readline().split())
    if tb * vb >= ta * va:
        print(tb * vb)
    else:
        # 상혁이 A를 x개 맡는 경우 (0 ~ va) 전부 시도
        best = 10**18
        for x in range(va + 1):
            time_sh = ta * x                         # 상혁 시간
            time_dh = ta * (va - x) + tb * vb        # 도훈 시간
            cur = max(time_sh, time_dh)
            if cur < best:
                best = cur
        print(best)
