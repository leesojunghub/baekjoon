import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    win = [0] * n
    lose = [0] * n
    for i in range(m):
        a, b, p, q = map(int, sys.stdin.readline().split())
        win[a-1] += p
        win[b-1] += q
        lose[a-1] += q
        lose[b-1] += p
    max = 0
    min = float('inf')
    for i in range(n):
        if win[i] == 0 and lose[i] == 0:
            score = 0.0
        else:
            score = (win[i] ** 2) / (win[i] ** 2 + lose[i] ** 2)
        if score > max:
            max = score
        if score < min:
            min = score
    print(int(max * 1000))
    print(int(min * 1000))