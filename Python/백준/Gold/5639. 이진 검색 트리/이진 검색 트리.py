import sys
sys.setrecursionlimit(10**7)
def build(min_val, max_val):
    global idx
    if idx >= n:
        return
    current = preorder[idx]
    if not (min_val < current < max_val):
        return
    idx += 1
    build(min_val, current)
    build(current, max_val)
    result.append(str(current))

preorder = list(map(int, sys.stdin.read().split()))
n = len(preorder)
idx = 0
result = []
build(-1, 10**7)
print("\n".join(result))
