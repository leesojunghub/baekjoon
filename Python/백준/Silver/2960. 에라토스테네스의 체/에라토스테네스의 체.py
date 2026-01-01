import sys
n, k = map(int, sys.stdin.readline().split())
base = [1]*(n+1)
base[0] = 0
base[1] = 0
count = 0
for i in range(2, n+1):
    if base[i]==1:
        for j in range(i,n+1,i):
            if base[j] == 1:
                base[j] = 0
                count += 1
                if count == k:
                    print(j)
                    exit()
                 
