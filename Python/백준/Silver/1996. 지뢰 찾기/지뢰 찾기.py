import sys
def find(x, y):
    global n
    if landmine[x][y] != '.':
        return "*"
    sum = 0
    for i in range(max(x-1, 0), min(x+2, n)):
        for j in range(max(y-1, 0), min(y+2, n)):
            if landmine[i][j] != '.':
                sum += int(landmine[i][j])
    if sum > 9:
        return "M"
    return str(sum)
n = int(sys.stdin.readline().strip())
landmine = []
for _ in range(n):
    a = list(sys.stdin.readline().strip())
    landmine.append(a)
map = [[-1] * n for _ in range(n)]
for i in range(0, n):
    for j in range(0, n):
        map[i][j] = find(i, j)
for row in map:
    print("".join(row))