import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
l.sort(key=lambda x: (-x[0], x[1]))
cnt = 0
prob = l[4][0]
i = 5
while i < n:
    if l[i][0] == prob:
        cnt += 1
        i += 1
    else:
        break
print(cnt)