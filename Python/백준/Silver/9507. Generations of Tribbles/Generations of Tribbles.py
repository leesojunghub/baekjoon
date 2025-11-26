import sys
def koong(n):
    while len(l) <= n:
        l.append(l[-1] + l[-2] + l[-3] + l[-4])
l = [1,1,2,4,8]
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    if n < len(l):
        print(l[n])
    else:
        koong(n)
        print(l[n])