import sys
s = sys.stdin.readline().strip()
for i in range(97, 123):
    print(s.count(chr(i)), end = ' ')