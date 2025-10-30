import sys, math
x, y = tuple(map(int, sys.stdin.readline().split()))
att = -50
for _ in range(11):
    a, b = map(int, sys.stdin.readline().split())
    if a > att:
        att = a
df_max = -50
df_scd = -50
for _ in range(11):
    a, b = map(int, sys.stdin.readline().split())
    if a > df_max:
        df_scd = df_max
        df_max = a
    elif a > df_scd:
        df_scd = a
if att > 0 and df_scd < att and att > x:
    print(1)
else:
    print(0)