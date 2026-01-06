import sys
l = list(map(int, sys.stdin.readline().split()))
while True:
    for i in range(0, 4):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            print(' '.join(map(str, l)))
        if l == [1,2,3,4,5]:
            exit()
