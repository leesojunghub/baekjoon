import sys
for line in sys.stdin:
    line = line.strip()
    n = len(line)
    for i in range(0, n, 2):
        print(chr(int(line[i:i+2],16)), end='')
    print()
    