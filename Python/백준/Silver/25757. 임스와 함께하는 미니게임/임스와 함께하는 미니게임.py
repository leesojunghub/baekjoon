import sys
n, game = sys.stdin.readline().strip().split()
name = set()
for _ in range(int(n)):
    a = sys.stdin.readline().strip()
    name.add(a)
cnt = len(name)
if game == 'Y':
    print(cnt)
elif game == 'F':
    print(cnt // 2)
elif game == 'O':
    print(cnt // 3)