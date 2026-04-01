import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    l = [1] * m
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            l[j] *= row[j]
    max_val = max(l)

    for i in range(m-1, -1, -1):
        if l[i] == max_val:
            print(i + 1)
            break
