import sys
n = int(sys.stdin.readline().strip())
for _ in range(n):
    s = sys.stdin.readline().strip()
    l = []
    s = s.lower()
    for i in range(97, 123):
        if chr(i) in s:
            pass
        else:
            l.append(chr(i))
    if len(l) == 0:
        print("pangram")
    else:
        print("missing", "".join(l))