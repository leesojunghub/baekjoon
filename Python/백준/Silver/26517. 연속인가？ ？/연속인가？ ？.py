import sys
k = int(sys.stdin.readline())
a,b,c,d = map(int, sys.stdin.readline().split())
if a*k+b == c*k+d:
    print('Yes', a*k+b)
else:
    print('No')