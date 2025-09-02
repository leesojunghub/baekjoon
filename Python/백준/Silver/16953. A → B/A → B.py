import sys

a, b = map(str, sys.stdin.readline().strip().split())
c = 1
while int(b) > int(a):
    if int(b) % 2 == 0:
        b = str(int(b) // 2)
        c += 1
    elif b[-1] == '1':
        b = b[:-1]
        c += 1
    else:
        break
if b == a:
    print(c)
else:
    print(-1)