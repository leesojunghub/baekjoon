import sys
def row(s):
    global r, c, w, h
    if s == '+':
        for _ in range(c):
            print('+'+'-'*w,end='')
        print('+')
    else:
        for _ in range(c):
            print('|'+'*'*w,end='')
        print('|')
t = int(sys.stdin.readline())
for i in range(1, t+1):
    r, c, w, h = map(int, sys.stdin.readline().split())
    print("Case #%d:"%i)
    for j in range(r*2+1):
        if j%2==0:
            row('+')
        else:
            for _ in range(h):
                row('|')