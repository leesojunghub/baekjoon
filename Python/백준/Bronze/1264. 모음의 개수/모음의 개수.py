import sys
while True:
    s = sys.stdin.readline().strip()
    if s == '#':
        break
    s = s.upper()
    c = 0
    c += s.count('A')
    c += s.count('E')
    c += s.count('I')
    c += s.count('O')
    c += s.count('U')
    print(c)