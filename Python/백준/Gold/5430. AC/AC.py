import sys
from collections import deque
t = int(sys.stdin.readline().strip())
for _ in range(t):
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    x = sys.stdin.readline().strip()
    x = x[1:-1]
    if x:
        x = deque(map(int, x.split(',')))
    else:
        x = deque()
    fb = True #기본 True = 앞
    error = False
    for i in p:
        if i == 'D':
            if not x:
                error = True
                break
            if fb:
                x.popleft()
            else:
                x.pop()
        elif i == 'R':
            fb = not fb
    if error:
        print('error')
    else:
        if fb:
            print(f"[{','.join(map(str, x))}]")
        else:
            print(f"[{','.join(map(str, reversed(x)))}]")
