import sys
input = sys.stdin.readline

def dfs(path, depth):
    if len(path) == m:
        if path == sorted(path):
            print(*path)
            return
        else:
            return
    for i in l:
        if i not in path:
            dfs(path + [i], depth + 1)

n, m = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
l.sort()
dfs([], 0)