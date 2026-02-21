import sys
n = int(sys.stdin.readline())
room = []
for _ in range(n):
    i = list(sys.stdin.readline().strip())
    room.append(i)
row = 0
col = 0
length = 0
for i in room:
    for j in i:
        if j == '.':
            length += 1
        else:
            if length >= 2:
                row += 1
            length = 0
    if length >= 2:
        row += 1
    length = 0
for i in range(n):
    for j in range(n):
        if room[j][i] == '.':
            length += 1
        else:
            if length >= 2:
                col += 1
            length = 0
    if length >= 2:
        col += 1
    length = 0

print(row, col)