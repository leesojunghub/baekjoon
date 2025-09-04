import sys
sys.setrecursionlimit(10000)
def dfs(x, y, color, field):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if field[x][y] == '0':
        return
    if field[x][y] != color:
        return
    global c
    field[x][y] = '0'
    dfs(x+1, y, color, field)
    dfs(x-1, y, color, field)
    dfs(x, y+1, color, field)
    dfs(x, y-1, color, field)
    
n = int(sys.stdin.readline().strip())
field = []
rg_field = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    field.append(list(s))
    rg_field.append(list(s.replace("G", "R")))
count = 0
for x in range(n):
    for y in range(n):
        if field[x][y] != '0':
            dfs(x, y, field[x][y], field)
            count += 1
rg_count = 0
for x in range(n):
    for y in range(n):
        if rg_field[x][y] != '0':
            dfs(x, y, rg_field[x][y], rg_field)
            rg_count += 1
print(count, rg_count)