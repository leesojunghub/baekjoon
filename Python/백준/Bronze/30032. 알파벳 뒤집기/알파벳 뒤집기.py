import sys
n, d = map(int, sys.stdin.readline().strip().split())
l = []
for _ in range(n):
    l.append(sys.stdin.readline().strip())
updown = {'d':'q', 'b':'p', 'q':'d', 'p':'b'}
leftrigt = {'d':'b', 'b':'d', 'q':'p', 'p':'q'}
answer = []
if d == 1:
    for i in l:
        s = ''
        for j in i:
            s += updown[j]
        answer.append(s)
else:
    for i in l:
        s = ''
        for j in i:
            s += leftrigt[j]
        answer.append(s)
for i in answer:
    print(i)