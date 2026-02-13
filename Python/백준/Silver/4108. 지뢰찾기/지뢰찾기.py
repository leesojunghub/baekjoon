import sys
def find_mine(i, j):
    if mine[i][j] == '*':
        return '*'
    cnt = 0
    for a in range(i-1, i+2):
        if a < 0:
            continue
        if a >= r:
            continue
        for b in range(j-1, j+2):
            if b < 0:
                continue
            if b >= c:
                continue
            if mine[a][b] == '*':
                cnt += 1
    return str(cnt)
while True:
    r, c = map(int, sys.stdin.readline().split())
    if r == 0 and c == 0:
        sys.exit()
    mine = []
    for _ in range(r):
        a =  list(sys.stdin.readline().strip())
        mine.append(a)
    land = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            land[i][j] = find_mine(i, j)
    for i in land:
        print(''.join(i))