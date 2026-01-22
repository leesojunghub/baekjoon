import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
for _ in range(q):
    quary = list(map(int, sys.stdin.readline().split()))
    if quary[0] == 1:
        now = a[quary[1]-1:quary[2]]
        print(now.count(quary[3]))
    else:
        a[quary[1]-1:quary[2]] = [-1] * (quary[2]-quary[1]+1)