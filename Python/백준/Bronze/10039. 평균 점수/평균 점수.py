import sys
l = []
for _ in range(5):
    n = int(sys.stdin.readline().strip())
    if n < 40:
        l.append(40)
    else:
        l.append(n)
print(int(sum(l)/5))