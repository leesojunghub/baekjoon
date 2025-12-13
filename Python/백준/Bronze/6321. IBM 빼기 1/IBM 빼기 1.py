import sys
n = int(sys.stdin.readline())
for i in range(1,n+1):
    s = sys.stdin.readline().strip()
    print('String #%d'%i)
    for j in s:
        k = ord(j)+1
        if k > 90:
            print('A', end='')
        else:
            print(chr(k), end='')
    print('\n')
