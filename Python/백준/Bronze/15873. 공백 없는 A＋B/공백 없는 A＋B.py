import sys
s = sys.stdin.readline().strip()
if s[1] == '0':
    print(int(s[:2])+ int(s[2:]))
else:
    print(int(s[:1])+ int(s[1:]))