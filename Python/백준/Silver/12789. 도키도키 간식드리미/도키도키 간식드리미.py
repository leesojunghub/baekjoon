import sys
input = sys.stdin.readline

n = int(input())
now = list(map(int, input().split()))
next = 1
other = []
for i in now:
    while other and other[-1] == next:
        other.pop()
        next += 1
    if i == next:
        next += 1
    else:
        other.append(i)
while other and other[-1] == next:
    other.pop()
    next += 1
if next == n + 1:
    print('Nice')
else:
    print('Sad')