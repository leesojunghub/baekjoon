n = int(input())
s = input().strip()

for i in range(2 * n-1):
    if s[i] == s[i+1]:
        print("No")
        break
else:
    print("Yes")