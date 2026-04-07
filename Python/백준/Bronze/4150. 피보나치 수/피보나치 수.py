import sys
input = sys.stdin.readline

n = int(input())
fi = [0,1,1,2,3]
if n < 5:
    print(fi[n])
    sys.exit()
for i in range(4,n):
    fi.append(fi[i] + fi[i-1])
print(fi[n])