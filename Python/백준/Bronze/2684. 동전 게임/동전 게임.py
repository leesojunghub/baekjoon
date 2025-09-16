import sys

p = int(sys.stdin.readline())
for _ in range(p):
    dic = {'TTT': 0, 'TTH': 0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0, 'HHT':0, 'HHH':0}
    s = sys.stdin.readline()
    for i in range(0, 38):
        dic[s[i:i+3]] += 1
    
    for i in dic:
        print(dic[i], end=' ')
    print()