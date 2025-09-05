import sys

def to_base(num, base):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    if num == 0:
        return digits[0]
    res = []
    while num > 0:
        res.append(digits[num % base])
        num //= base
    return ''.join(reversed(res))

t = int(sys.stdin.readline().strip())
for _ in range(t):
    palindrome = False
    n = int(sys.stdin.readline().strip())
    for i in range(2, 65):
        a = to_base(n, i)
        if a == a[::-1]:
            palindrome = True
            break
    if palindrome:
        print(1)
    else:
        print(0)