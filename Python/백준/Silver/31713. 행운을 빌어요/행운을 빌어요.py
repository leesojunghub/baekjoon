import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    result = 0
    if a * 4 < b:
        need = b - 4 * a
        add_stem = (need + 3) // 4   # ceil(need/4)
        a += add_stem
        result += add_stem

    # 2) 3*a <= b 되게 잎 추가
    if 3 * a > b:
        result += 3 * a - b

    print(result)