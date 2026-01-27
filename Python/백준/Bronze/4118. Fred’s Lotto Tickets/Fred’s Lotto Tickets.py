import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    need = set(range(1, 50))
    inp = set()
    for _ in range(n):
        a = set(map(int, sys.stdin.readline().split()))
        inp.update(a)
    if need == inp:
        print('Yes')
    else:
        print('No')