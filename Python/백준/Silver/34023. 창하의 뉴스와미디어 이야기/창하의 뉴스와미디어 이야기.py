import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    s, d = sys.stdin.readline().strip().split()
    l.append((int(d), s))
l.sort(reverse=True)
c = [[],[],[],[]]
for i in range(n):
    d, s = l[i]
    c[i%4].append(s)
for i in range(4):
    c[i].sort()
    print(i+1, ' '.join(c[i]))