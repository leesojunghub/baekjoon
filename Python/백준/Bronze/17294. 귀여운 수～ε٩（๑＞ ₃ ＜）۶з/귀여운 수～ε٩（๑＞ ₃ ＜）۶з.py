import sys
k = list(sys.stdin.readline().strip())
n = len(k)
if n < 3:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    gap = int(k[1]) - int(k[0])
    for i in range(1, n-1):
        if int(k[i]) + gap != int(k[i+1]):
            print('흥칫뿡!! <(￣ ﹌ ￣)>')
            exit()
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')