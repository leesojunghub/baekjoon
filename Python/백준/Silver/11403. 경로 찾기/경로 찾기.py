import sys

n = int(sys.stdin.readline())
m = []
for _ in range(n):
    l = list(sys.stdin.readline().split())
    m.append(l)
# for i in range(n):
#     m[i][i] = '1'
for k in range(n):
    for i in range(n):
        if m[i][k] == '1':
            for j in range(n):
                if m[k][j] == '1':
                    m[i][j] = '1'
for i in m:
    print(' '.join(i))