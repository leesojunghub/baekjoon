import sys
n = int(sys.stdin.readline())
for _ in range(n):
    l = list(sys.stdin.readline().strip().split())
    l[0] = 'god'
    print(''.join(l))
