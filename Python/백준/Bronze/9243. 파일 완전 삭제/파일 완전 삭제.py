import sys
input = sys.stdin.readline

n = int(input())
a = input().strip()
b = input().strip()
if n % 2 == 0:
    if a == b:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            print('Deletion failed')
            sys.exit()
    print('Deletion succeeded')