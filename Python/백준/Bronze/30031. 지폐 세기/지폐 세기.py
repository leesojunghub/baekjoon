import sys
n = int(sys.stdin.readline())
dic = {136: 1000, 142:5000, 148:10000, 154:50000}
total = 0
for i in range(1,n+1):
    width, height = map(int,sys.stdin.readline().split())
    total += dic[width]
print(total)