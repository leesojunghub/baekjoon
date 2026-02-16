import sys
n = int(sys.stdin.readline())
st = sys.stdin.readline().strip()
cnt = 0
for i in range(0, n // 2):
    if st[i] != st[-1 * (i+1)]:
        cnt += 1
print(cnt)