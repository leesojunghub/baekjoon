import sys
import bisect
n = int(sys.stdin.readline())
sg = []
gs = []
for _ in range(n):
    a = int(sys.stdin.readline())
    sg.append(a)
set_sg = set(sg)
for i in range(1, 2 * n + 1):
    if i in set_sg:
        pass
    else:
        gs.append(i)
sg.sort()
gs.sort()
last = 0
turn = 0
while len(sg) != 0 and len(gs) != 0:
    if turn == 0:
        last_x = bisect.bisect_right(sg, last)
        if last_x >= len(sg):
            last = 0
            turn = 1
        else:
            last = sg[last_x]
            del sg[last_x]
            turn = 1
    else:
        last_x = bisect.bisect_right(gs, last)
        if last_x >= len(gs):
            last = 0
            turn = 0
        else:
            last = gs[last_x]
            del gs[last_x]
            turn = 0
print(len(gs))
print(len(sg))