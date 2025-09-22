import sys
while True:
    s = sys.stdin.readline().strip()
    if s == '#':
        break
    c = s.count("1")
    if s[-1] == 'e':
        if c % 2 == 0:
            print(s[:-1]+'0')
        else:
            print(s[:-1]+'1')
    else:
        if c % 2 == 0:
            print(s[:-1]+'1')
        else:
            print(s[:-1]+'0')