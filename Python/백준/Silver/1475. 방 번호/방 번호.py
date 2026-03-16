import sys
from collections import Counter
input = sys.stdin.readline

s = input().strip()
c = Counter(s)
if (c['6'] + c['9']) % 2 == 0:
    c['6'] = (c['6'] + c['9']) // 2
    c['9'] = 0
else:
    c['6'] = (c['6'] + c['9']) // 2 + 1
    c['9'] = 0
print(max(c.values()))