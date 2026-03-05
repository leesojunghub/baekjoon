import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
l = deque(range(1, n + 1))
while l:
    a = l.popleft()
    print(a, end=' ')
    if l:
        a = l.popleft()
        l.append(a)