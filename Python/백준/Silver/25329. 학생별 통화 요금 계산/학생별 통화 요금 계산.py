import sys
import math
n = int(sys.stdin.readline().strip())
dic = {}
for _ in range(n):
    time, name = sys.stdin.readline().strip().split()
    hour, minuate = map(int, time.split(':'))
    if name in dic:
        dic[name] += hour * 60 + minuate
    else:
        dic[name] = hour * 60 + minuate
money = {}
for i in dic:
    if dic[i] > 100:
        money[i] = 10 + math.ceil((dic[i] - 100) / 50) * 3
    else:
        money[i] = 10
sorted_list = sorted(money.items(), key=lambda x: (-x[1], x[0]))
for name, fee in sorted_list:
    print(name, fee)