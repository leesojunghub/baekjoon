import sys
input = sys.stdin.readline

u, o, s = list(map(int, input().split()))
cnt = min(u, s, o)
u -= cnt
s -= cnt
o -= cnt
s += u // 3
u -= 2 * (u // 3)
cnt += min(u, s, o)
print(cnt)