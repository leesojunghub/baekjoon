import sys
from collections import deque
w = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
queue = deque()
t = 0
out = True
s = 0
c = 0
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    if out:
        if c < 4:
            queue.append(a)
            s += a
            c += 1
            if s > w:
                out = False
            else:
                t += 1
        else:
            queue.append(a)
            s = s + a - queue.popleft()
            if s > w:
                out = False
            else:
                t += 1
print(t)