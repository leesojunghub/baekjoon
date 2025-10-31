import sys, math
while True:
    l = list(map(int, sys.stdin.readline().split()))
    if l[0] == 0:
        break
    last = 0
    for i in range(1, l[0]+1):
        if l[i] == last:
            pass
        else:
            print(l[i], end = ' ')
            last = l[i]
    print('$')