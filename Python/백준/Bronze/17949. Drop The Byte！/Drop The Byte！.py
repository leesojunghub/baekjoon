import sys

s = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
l = list(sys.stdin.readline().split())
i = 0
for type in l:
    if type == 'char':
        print(int(s[i:i+2], 16), end=' ')
        i += 2
    elif type == 'int':
        print(int(s[i:i+8], 16), end=' ')
        i += 8
    elif type == 'long_long':
        print(int(s[i:i+16], 16), end=' ')
        i += 16